# fix_gitbook_links_format_v2.py
# Usage (Windows example):
# python "C:\MyCode\GitBook\Omni-Wiki-Rejean-King-Klown\fix_gitbook_links_format_v2.py" ^
#   --root "C:\MyCode\GitBook\Omni-Wiki-Rejean-King-Klown" --repo "https://github.com/ORG/REPO" --branch main
#
# What it fixes:
# 1) Rewrites "root-style" markdown links like (03-vote/xx.md) into file-relative links (../03-vote/xx.md).
# 2) Converts inline-code file refs like `03-vote/xx.md` into clickable links, when the target file exists.
#    (Leaves non-existent or non-.md code spans untouched.)
#
# Safe guards:
# - Does NOT change anything inside fenced code blocks (``` ... ```).
# - Skips external links (http:, https:, mailto:, etc.) and pure anchors (#...).
#
# Notes:
# - The --repo and --branch args are accepted for compatibility with your command line,
#   but are not required for the link/format fixes. (They are available for future extensions.)

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Tuple

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")
FENCE_RE = re.compile(r"^\s*(```|~~~)")  # fenced code blocks
# Basic markdown link/image: [text](target) or ![alt](target)
MD_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
# Inline code: `something`
INLINE_CODE_RE = re.compile(r"`([^`]+)`")

def is_external_or_anchor(target: str) -> bool:
    t = target.strip()
    if not t:
        return True
    if t.startswith("#"):
        return True
    if SCHEME_RE.match(t):
        return True
    return False

def split_path_and_suffix(target: str) -> Tuple[str, str]:
    """
    Splits (path + optional #anchor/?query) while preserving suffix.
    Example: "a/b.md#x" -> ("a/b.md", "#x")
    """
    t = target.strip()
    m = re.search(r"[?#]", t)
    if m:
        return t[:m.start()], t[m.start():]
    return t, ""

def normalize_rel(rel: str) -> str:
    rel = rel.replace(os.sep, "/")
    # If it is a simple filename ("x.md"), prefer "./x.md" for clarity
    if "/" not in rel and not rel.startswith("."):
        rel = "./" + rel
    return rel

def resolve_target(root: Path, path_part: str) -> Path | None:
    """
    Treats path_part as "root-style" (relative to root) and resolves if it exists.
    """
    if not path_part or path_part.startswith(".") or path_part.startswith("/"):
        return None
    candidate = (root / path_part).resolve()
    if candidate.exists():
        return candidate
    return None

def rewrite_markdown_links(line: str, md_path: Path, root: Path) -> Tuple[str, int]:
    """
    Rewrite markdown link targets that look like root-relative paths (e.g., 03-vote/x.md)
    into file-relative links from md_path.
    """
    rewrites = 0

    def _repl(m: re.Match) -> str:
        nonlocal rewrites
        prefix, target, suffix_paren = m.group(1), m.group(2), m.group(3)
        raw = target.strip()

        if is_external_or_anchor(raw):
            return m.group(0)

        path_part, suffix = split_path_and_suffix(raw)

        # Keep already file-relative or absolute-root links unchanged
        if path_part.startswith(".") or path_part.startswith("/"):
            return m.group(0)

        abs_target = resolve_target(root, path_part)
        if abs_target is None:
            return m.group(0)

        rel = os.path.relpath(abs_target, start=md_path.parent.resolve())
        rel = normalize_rel(rel)
        new_target = rel + suffix

        if new_target != raw:
            rewrites += 1
            return f"{prefix}{new_target}{suffix_paren}"
        return m.group(0)

    return MD_LINK_RE.sub(_repl, line), rewrites

def convert_inline_code_paths(line: str, md_path: Path, root: Path) -> Tuple[str, int]:
    """
    Converts inline code spans that reference existing .md files into clickable links.
    Example: `03-vote/00-vote-overview.md` -> [`03-vote/00-vote-overview.md`](../03-vote/00-vote-overview.md)
    """
    conversions = 0

    def looks_like_md_path(s: str) -> bool:
        ss = s.strip()
        # Must look like a markdown file path
        if not ss.lower().endswith(".md"):
            return False
        # Must contain at least a slash OR be a common top-level doc
        if "/" in ss or ss in {"README.md", "SUMMARY.md"}:
            return True
        return False

    def _repl(m: re.Match) -> str:
        nonlocal conversions
        code = m.group(1).strip()

        if not looks_like_md_path(code):
            return m.group(0)

        # Do not touch if it's already a markdown link label inside backticks like [`x`](...)
        # (Heuristic: if immediately preceded by "[" in the original line, skip.)
        # We can't easily check exact position without more parsing, so keep it simple.

        abs_target = resolve_target(root, code)
        if abs_target is None:
            return m.group(0)

        rel = os.path.relpath(abs_target, start=md_path.parent.resolve())
        rel = normalize_rel(rel)
        conversions += 1
        # Preserve the visible text as the path, but turn it into a link
        return f"[`{code}`]({rel})"

    return INLINE_CODE_RE.sub(_repl, line), conversions

def process_file(md_path: Path, root: Path, dry_run: bool) -> Tuple[int, int]:
    original = md_path.read_text(encoding="utf-8")
    lines = original.splitlines(True)

    in_fence = False
    link_rewrites = 0
    code_conversions = 0

    out_lines: list[str] = []

    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        # 1) Rewrite markdown links
        line2, r1 = rewrite_markdown_links(line, md_path, root)
        link_rewrites += r1

        # 2) Convert inline-code md paths to clickable links
        line3, r2 = convert_inline_code_paths(line2, md_path, root)
        code_conversions += r2

        out_lines.append(line3)

    new_text = "".join(out_lines)

    if new_text != original and not dry_run:
        md_path.write_text(new_text, encoding="utf-8")

    return link_rewrites, code_conversions

def should_skip_dir(p: Path) -> bool:
    parts = {x.lower() for x in p.parts}
    return any(x in parts for x in {".git", "node_modules", ".venv", "venv", "__pycache__", ".idea", ".vscode"})

def main() -> None:
    ap = argparse.ArgumentParser(description="Fix GitBook markdown link formatting and convert code-path refs to links.")
    ap.add_argument("--root", type=Path, required=True, help="Repo root containing the markdown files.")
    ap.add_argument("--repo", type=str, default="", help="Repo URL (accepted; not required for fixes).")
    ap.add_argument("--branch", type=str, default="main", help="Repo branch (accepted; not required for fixes).")
    ap.add_argument("--dry-run", action="store_true", help="Do not write changes; only report.")
    args = ap.parse_args()

    root = args.root.resolve()
    if not root.exists():
        raise SystemExit(f"--root does not exist: {root}")

    md_files: list[Path] = []
    for p in root.rglob("*.md"):
        if should_skip_dir(p):
            continue
        md_files.append(p)

    total_link_rewrites = 0
    total_code_conversions = 0
    changed_files = 0

    for f in sorted(md_files):
        before = f.read_text(encoding="utf-8")
        r_links, r_codes = process_file(f, root, dry_run=args.dry_run)
        after = before if args.dry_run else f.read_text(encoding="utf-8")

        if (r_links + r_codes) > 0:
            changed_files += 1
            rel = f.relative_to(root)
            print(f"{rel}: {r_links} link rewrites, {r_codes} code-path conversions")

        total_link_rewrites += r_links
        total_code_conversions += r_codes

    mode = "DRY RUN" if args.dry_run else "WROTE"
    print(f"{mode}: {changed_files} files changed; {total_link_rewrites} links rewritten; {total_code_conversions} code refs converted.")

    # Quick warning for empty README
    readme = root / "README.md"
    if readme.exists():
        txt = readme.read_text(encoding="utf-8")
        if not txt.strip():
            print("WARNING: README.md is empty. GitBook home page will be blank unless you populate it or change the entry page.")

if __name__ == "__main__":
    main()
