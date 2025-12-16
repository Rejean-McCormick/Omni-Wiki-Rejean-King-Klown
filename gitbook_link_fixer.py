#!/usr/bin/env python3
"""
gitbook_link_fixer.py

Batch-fix Markdown links so GitBook treats them as internal pages instead of falling back to GitHub.

Two common setups:
  A) GitBook syncs the repo root (or a docs root that already contains *all* referenced files).
     -> This script normalizes links and reports any that escape the docs root.

  B) GitBook syncs a subfolder (monorepo "Project directory" or .gitbook.yaml root) like KK-fr/.
     Some links like ../corps/orgo.md escape the docs root, so GitBook can't resolve them and may link to GitHub.
     -> Use --vendor to copy referenced .md files from outside docs root into it (mirroring paths),
        and rewrite links to point to the vendored copy.

Safe defaults:
  - Dry-run by default (no changes)
  - Creates backups when --write is used (unless --no-backup)
"""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Tuple, Dict, Set


SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")

# Inline Markdown links: [text](dest "optional title") and reference definitions: [id]: dest "title"
# This is intentionally conservative: we skip code fences and we don't touch images (![]()).
INLINE_LINK_RE = re.compile(r'(?P<img>!)?\[(?P<text>[^\]]*?)\]\((?P<dest>[^)\n]+?)\)')
REF_DEF_RE = re.compile(r'^(?P<id>\[[^\]]+\]):\s*(?P<dest>\S+)(?P<rest>\s+.*)?$')


@dataclass(frozen=True)
class LinkParts:
    raw: str          # full raw destination as found inside (...)
    base: str         # path without query/fragment and without surrounding <>
    query: str        # includes leading '?', or ''
    frag: str         # includes leading '#', or ''
    title: str        # anything after a whitespace in dest (e.g., "Title"), including leading space, or ''


def split_dest(dest: str) -> LinkParts:
    raw = dest.strip()
    title = ""
    # Handle optional title: split on first whitespace not inside <>.
    # This is a heuristic; works for the common cases in repos.
    if raw.startswith("<"):
        # angle-bracketed URL (rare in your repo, but supported by Markdown)
        # title may still follow after >
        end = raw.find(">")
        if end != -1:
            base_part = raw[: end + 1]
            rest = raw[end + 1 :].lstrip()
            if rest:
                title = " " + rest
            raw = base_part.strip()
    else:
        # split at first whitespace
        m = re.search(r'\s', raw)
        if m:
            title = raw[m.start():]
            raw = raw[:m.start()]

    # strip <...>
    base0 = raw
    if base0.startswith("<") and base0.endswith(">"):
        base0 = base0[1:-1].strip()

    # fragment after query by URL rules, but easiest is split '#' first then '?' on the left part
    frag = ""
    if "#" in base0:
        left, f = base0.split("#", 1)
        base0 = left
        frag = "#" + f

    query = ""
    if "?" in base0:
        left, q = base0.split("?", 1)
        base0 = left
        query = "?" + q

    return LinkParts(raw=dest, base=base0, query=query, frag=frag, title=title)


def is_external(href_base: str) -> bool:
    hb = href_base.strip()
    return hb.startswith(SCHEMES) or hb.startswith("//")


def norm_posix(p: str) -> str:
    return p.replace("\\", "/")


def rel_from(file_path: Path, root: Path) -> str:
    return norm_posix(file_path.relative_to(root).as_posix())


def within_root(rel_posix_path: str) -> bool:
    return rel_posix_path != ".." and not rel_posix_path.startswith("../") and rel_posix_path != "."


def resolve_target_rel(file_rel: str, href_base: str) -> str:
    """
    Resolve href_base (posix) relative to file_rel (posix path from root),
    returning normalized posix path relative to root.
    """
    href_base = norm_posix(href_base)
    if href_base.startswith("/"):
        candidate = href_base.lstrip("/")
    else:
        cur_dir = posixpath.dirname(file_rel)
        candidate = posixpath.join(cur_dir, href_base)
    candidate = posixpath.normpath(candidate)
    return candidate


def pick_existing_md(repo_root: Path, target_rel: str) -> Optional[str]:
    """
    For extensionless links, try common Markdown filenames.
    Returns the relative path that exists, or None.
    """
    # If it already has an extension, just check existence
    t = Path(target_rel)
    if t.suffix:
        return target_rel if (repo_root / target_rel).exists() else None

    # Try target as-is (some repos have extensionless files)
    if (repo_root / target_rel).exists():
        return target_rel

    # Try adding .md
    if (repo_root / (target_rel + ".md")).exists():
        return target_rel + ".md"

    # Try README.md inside directory
    if (repo_root / target_rel / "README.md").exists():
        return posixpath.join(target_rel, "README.md")

    return None


def rewrite_href(
    file_rel: str,
    href: str,
    docs_root: Path,
    repo_root: Path,
    strip_md_ext: bool,
    readme_as_index: bool,
    vendor: bool,
    vendored: Set[str],
    copied: Set[Tuple[str, str]],
) -> Tuple[str, Optional[str]]:
    """
    Returns (new_href, warning) where warning is a message if the link escapes docs_root or is broken.
    """
    parts = split_dest(href)
    base = parts.base.strip()
    if not base or is_external(base) or base.startswith("#"):
        return href, None

    base = norm_posix(base)

    file_rel_posix = norm_posix(file_rel)

    target_rel = resolve_target_rel(file_rel_posix, base)

    # Try to map extensionless links to actual Markdown files
    existing_rel = pick_existing_md(repo_root, target_rel)
    if existing_rel is None:
        # Still rewrite pure path normalization if it stays within docs_root,
        # but emit warning.
        existing_rel = target_rel

    # Determine whether target is within docs_root
    docs_rel = rel_from(repo_root / existing_rel, repo_root)  # normalized
    # Compute relative to docs_root for "within" test
    try:
        rel_to_docs = norm_posix((repo_root / existing_rel).relative_to(docs_root).as_posix())
        inside_docs = True
    except ValueError:
        inside_docs = False
        rel_to_docs = ""

    if not inside_docs:
        if not vendor:
            return href, f"ESCAPES_DOCS_ROOT -> {existing_rel}"
        # Vendor: copy into docs_root, mirroring path relative to repo root
        # Example: repo_root/corps/orgo.md -> docs_root/corps/orgo.md
        src = repo_root / existing_rel
        if not src.exists():
            return href, f"BROKEN_OR_MISSING (cannot vendor) -> {existing_rel}"

        dst = docs_root / existing_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            shutil.copy2(src, dst)
            copied.add((str(src), str(dst)))
        vendored.add(existing_rel)

        # Now the target is inside docs_root by construction, and we want a relative link from current file
        # within docs_root
        # file_rel within docs_root:
        try:
            file_rel_to_docs = norm_posix((repo_root / file_rel_posix).relative_to(docs_root).as_posix())
        except ValueError:
            # current file is not within docs_root; caller should only process files under docs_root
            file_rel_to_docs = file_rel_posix

        cur_dir = posixpath.dirname(file_rel_to_docs)
        new_base = posixpath.relpath(existing_rel, start=cur_dir) if cur_dir else existing_rel
        new_base = norm_posix(new_base)

    else:
        # Keep it internal to docs_root: prefer a relative link from current file within docs_root
        file_rel_to_docs = norm_posix((repo_root / file_rel_posix).relative_to(docs_root).as_posix())
        cur_dir = posixpath.dirname(file_rel_to_docs)
        # rel_to_docs is the path of the target inside docs_root
        new_base = posixpath.relpath(rel_to_docs, start=cur_dir) if cur_dir else rel_to_docs
        new_base = norm_posix(new_base)

    # Optional: turn .../README.md into .../ (index)
    if readme_as_index and (new_base == "README.md" or new_base.endswith("/README.md")):
        new_base = new_base[: -len("README.md")]
        new_base = new_base.rstrip("/") or "."  # keep something valid

    if strip_md_ext and new_base.endswith(".md"):
        new_base = new_base[:-3]

    rebuilt = new_base + parts.query + parts.frag
    # Re-apply angle brackets only if original used them (rare); avoid changing semantics
    # Preserve title (if any)
    if parts.raw.strip().startswith("<") and parts.raw.strip().endswith(">") and not parts.title:
        rebuilt = f"<{rebuilt}>"
    rebuilt = rebuilt + parts.title

    return rebuilt, None


def iter_md_files(root: Path, exts: Tuple[str, ...], ignore_dirs: Set[str]) -> Iterable[Path]:
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        if p.suffix.lower() not in exts:
            continue
        # ignore directories
        if any(part in ignore_dirs for part in p.parts):
            continue
        yield p


def rewrite_file(
    md_path: Path,
    docs_root: Path,
    repo_root: Path,
    strip_md_ext: bool,
    readme_as_index: bool,
    vendor: bool,
    vendored: Set[str],
    copied: Set[Tuple[str, str]],
) -> Tuple[str, int, int, Set[str]]:
    """
    Returns (new_text, changed_count, link_count, warnings)
    """
    text = md_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(True)

    in_fence = False
    changed = 0
    total_links = 0
    warnings: Set[str] = set()

    file_rel = rel_from(md_path, repo_root)

    def repl_inline(m: re.Match) -> str:
        nonlocal changed, total_links
        if m.group("img"):  # don't touch images
            return m.group(0)
        dest = m.group("dest")
        total_links += 1
        new_dest, warn = rewrite_href(
            file_rel=file_rel,
            href=dest,
            docs_root=docs_root,
            repo_root=repo_root,
            strip_md_ext=strip_md_ext,
            readme_as_index=readme_as_index,
            vendor=vendor,
            vendored=vendored,
            copied=copied,
        )
        if warn:
            warnings.add(warn)
        if new_dest != dest:
            changed += 1
            return m.group(0).replace(f"({dest})", f"({new_dest})", 1)
        return m.group(0)

    out_lines = []
    for line in lines:
        # crude code fence detection
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        # reference definitions
        mdef = REF_DEF_RE.match(line)
        if mdef:
            dest = mdef.group("dest")
            total_links += 1
            new_dest, warn = rewrite_href(
                file_rel=file_rel,
                href=dest,
                docs_root=docs_root,
                repo_root=repo_root,
                strip_md_ext=strip_md_ext,
                readme_as_index=readme_as_index,
                vendor=vendor,
                vendored=vendored,
                copied=copied,
            )
            if warn:
                warnings.add(warn)
            if new_dest != dest:
                changed += 1
                rest = mdef.group("rest") or ""
                out_lines.append(f"{mdef.group('id')}: {new_dest}{rest}\n" if not line.endswith("\n") else f"{mdef.group('id')}: {new_dest}{rest}")
            else:
                out_lines.append(line)
            continue

        # inline links
        new_line = INLINE_LINK_RE.sub(repl_inline, line)
        out_lines.append(new_line)

    return ("".join(out_lines), changed, total_links, warnings)


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch-fix Markdown links for GitBook.")
    ap.add_argument("--repo-root", default=".", help="Repository root (default: current directory).")
    ap.add_argument("--docs-root", default=".", help="GitBook docs root (default: same as repo root).")
    ap.add_argument("--ext", action="append", default=[".md"], help="File extension to process (repeatable). Default: .md")
    ap.add_argument("--ignore-dir", action="append", default=[".git", "node_modules", ".venv", "dist", "build", "_book", ".next"], help="Directory name to ignore (repeatable).")
    ap.add_argument("--strip-md-ext", action="store_true", help="Rewrite links to remove the trailing .md")
    ap.add_argument("--no-readme-index", action="store_true", help="Do not rewrite README.md links as folder index links")
    ap.add_argument("--vendor", action="store_true", help="If a link escapes docs root, copy the target Markdown file into docs root and rewrite to that copy.")
    ap.add_argument("--write", action="store_true", help="Write changes in-place (default: dry-run).")
    ap.add_argument("--no-backup", action="store_true", help="Do not create .bak backups when writing.")
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    docs_root = (repo_root / args.docs_root).resolve() if not Path(args.docs_root).is_absolute() else Path(args.docs_root).resolve()

    if not docs_root.exists():
        print(f"ERROR: docs-root does not exist: {docs_root}", file=sys.stderr)
        return 2

    exts = tuple(e if e.startswith(".") else f".{e}" for e in args.ext)
    ignore_dirs = set(args.ignore_dir)

    md_files = list(iter_md_files(docs_root, exts, ignore_dirs))
    if not md_files:
        print(f"No files found under {docs_root} with extensions {exts}.")
        return 0

    total_changed_links = 0
    total_links = 0
    files_changed = 0
    all_warnings: Dict[str, Set[str]] = {}
    vendored: Set[str] = set()
    copied: Set[Tuple[str, str]] = set()

    for f in md_files:
        new_text, changed, links, warnings = rewrite_file(
            md_path=f,
            docs_root=docs_root,
            repo_root=repo_root,
            strip_md_ext=args.strip_md_ext,
            readme_as_index=not args.no_readme_index,
            vendor=args.vendor,
            vendored=vendored,
            copied=copied,
        )
        total_changed_links += changed
        total_links += links

        if changed and args.write:
            if not args.no_backup:
                bak = f.with_suffix(f.suffix + ".bak")
                if not bak.exists():
                    shutil.copy2(f, bak)
            f.write_text(new_text, encoding="utf-8")
            files_changed += 1
        elif changed:
            files_changed += 1  # would change

        if warnings:
            all_warnings[rel_from(f, docs_root)] = warnings

    # Summary
    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"[{mode}] Processed {len(md_files)} files under docs root: {docs_root}")
    print(f"[{mode}] Found {total_links} links; would change {total_changed_links} link(s) in {files_changed} file(s).")
    if args.vendor:
        print(f"[{mode}] Vendored {len(vendored)} external-to-docs file(s); copied {len(copied)} file(s).")
        # print copies (compact)
        for src, dst in sorted(copied)[:50]:
            print(f"  COPIED: {src} -> {dst}")
        if len(copied) > 50:
            print(f"  ... {len(copied)-50} more")

    if all_warnings:
        print(f"[{mode}] Warnings (links that still escape docs root or are missing):")
        for file_rel, warns in sorted(all_warnings.items()):
            for w in sorted(warns):
                print(f"  {file_rel}: {w}")

    if not args.write:
        print("Tip: re-run with --write to apply changes. Backups are created as *.md.bak unless --no-backup.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
