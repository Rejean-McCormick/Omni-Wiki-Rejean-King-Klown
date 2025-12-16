#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse, unquote

MD_EXTS = {".md", ".markdown", ".mdx"}

OAICITE_RE = re.compile(r":contentReference\[oaicite:[^\]]+\]\{[^}]*\}")
CITE_BRACKET_RE = re.compile(r"\[cite(?::[^\]]+)?\]|\[cite_start\]|\[cite_end\]", re.IGNORECASE)
CITE_INLINE_RE = re.compile(r"\[\s*cite\s*:\s*[^]]+\]", re.IGNORECASE)
CONTENT_REFERENCE_GENERIC_RE = re.compile(r":contentReference\[[^\]]+\]\{[^}]*\}")

MD_LINK_RE = re.compile(
    r"(?P<prefix>!?\[.*?\])\((?P<target>\s*<?[^)\s>]+>?)(?P<rest>\s+\"[^\"]*\"|\s+'[^']*'|\s*)\)",
    re.DOTALL,
)
HTML_HREF_RE = re.compile(r"""(?P<attr>\b(?:href|src)\s*=\s*)(?P<q>["'])(?P<val>.*?)(?P=q)""", re.IGNORECASE)

@dataclass
class Change:
    file: Path
    changed: bool
    notes: List[str]

def normalize_slashes(s: str) -> str:
    return s.replace("\\", "/")

def strip_angle(s: str) -> str:
    s = s.strip()
    return s[1:-1].strip() if s.startswith("<") and s.endswith(">") else s

def split_anchor(s: str) -> Tuple[str, str]:
    if "#" in s:
        b, a = s.split("#", 1)
        return b, "#" + a
    return s, ""

def is_url(s: str) -> bool:
    u = urlparse(s)
    return bool(u.scheme)

def default_prefix_map() -> Dict[str, str]:
    return {"/fr": "KK-fr", "/en": "KK-en", "/rejean": "Rejean-en", "/Rejean": "Rejean-en"}

def apply_prefix_map(path: str, pmap: Dict[str, str]) -> str:
    for prefix in sorted(pmap.keys(), key=len, reverse=True):
        if path == prefix or path.startswith(prefix + "/"):
            mapped = pmap[prefix]
            rest = path[len(prefix):].lstrip("/")
            return f"{mapped}/{rest}".rstrip("/")
    return path

def parse_repo(repo_url: Optional[str]) -> Optional[Tuple[str, str]]:
    if not repo_url:
        return None
    u = urlparse(repo_url)
    if u.netloc.lower() != "github.com":
        return None
    parts = [p for p in u.path.split("/") if p]
    return (parts[0], parts[1]) if len(parts) >= 2 else None

def github_to_path(url: str, repo: Optional[Tuple[str, str]], branch: Optional[str]) -> Optional[str]:
    u = urlparse(url)
    host = u.netloc.lower()
    path = unquote(u.path or "")
    if host == "github.com":
        parts = [p for p in path.split("/") if p]
        if len(parts) < 5:
            return None
        org, rep, kind, br = parts[0], parts[1], parts[2], parts[3]
        if repo and (org != repo[0] or rep != repo[1]):
            return None
        if branch and br != branch:
            return None
        if kind not in ("blob", "tree"):
            return None
        rest = "/".join(parts[4:])
        if kind == "tree" and rest and not rest.endswith("/"):
            rest += "/"
        return rest or None
    if host == "raw.githubusercontent.com":
        parts = [p for p in path.split("/") if p]
        if len(parts) < 4:
            return None
        org, rep, br = parts[0], parts[1], parts[2]
        if repo and (org != repo[0] or rep != repo[1]):
            return None
        if branch and br != branch:
            return None
        return "/".join(parts[3:]) or None
    return None

def clean_text(text: str) -> str:
    text = OAICITE_RE.sub("", text)
    text = CONTENT_REFERENCE_GENERIC_RE.sub("", text)
    text = CITE_BRACKET_RE.sub("", text)
    text = CITE_INLINE_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

def fix_target(raw: str, pmap: Dict[str, str], repo: Optional[Tuple[str, str]], branch: Optional[str]) -> Tuple[str, List[str]]:
    notes: List[str] = []
    t = normalize_slashes(strip_angle(raw)).strip()
    if not t:
        return raw, notes
    base, anchor = split_anchor(t)

    # Convert GitHub links (otherwise GitBook navigates out to GitHub)
    if is_url(base):
        rp = github_to_path(base, repo, branch)
        if rp:
            notes.append(f"github->relative {base} -> {rp}")
            base = rp
        else:
            return raw, notes

    # Map /fr/... style to repo folders
    if base.startswith("/"):
        mapped = apply_prefix_map(base, pmap)
        if mapped != base:
            notes.append(f"prefix {base} -> {mapped}")
        base = mapped.lstrip("/")

    if base.lower().endswith(".ipynb"):
        base = base[:-6] + ".md"
        notes.append("ipynb->md")

    low = base.lower()
    if low.endswith("index.md") or low.endswith("index.mdx") or low.endswith("index.markdown") or low.endswith("notebookindex.md"):
        base = str(Path(base).with_name("README.md")).replace("\\", "/")
        notes.append("index->README")

    if base.endswith("/"):
        base = base.rstrip("/") + "/README.md"
        notes.append("dir->README")

    fixed = base + anchor
    return (f"<{fixed}>" if raw.strip().startswith("<") and raw.strip().endswith(">") else fixed), notes

def rewrite_links(text: str, pmap: Dict[str, str], repo: Optional[Tuple[str, str]], branch: Optional[str]) -> Tuple[str, int]:
    changes = 0

    def repl(m: re.Match) -> str:
        nonlocal changes
        prefix, target, rest = m.group("prefix"), m.group("target"), m.group("rest") or ""
        fixed, _ = fix_target(target, pmap, repo, branch)
        if fixed != target:
            changes += 1
        return f"{prefix}({fixed}{rest})"

    text2 = MD_LINK_RE.sub(repl, text)

    def repl_html(m: re.Match) -> str:
        nonlocal changes
        attr, q, val = m.group("attr"), m.group("q"), m.group("val")
        fixed, _ = fix_target(val, pmap, repo, branch)
        if fixed != val:
            changes += 1
        return f"{attr}{q}{fixed}{q}"

    text3 = HTML_HREF_RE.sub(repl_html, text2)
    return text3, changes

def collect_targets(text: str) -> List[str]:
    out: List[str] = []
    out += [m.group("target").strip() for m in MD_LINK_RE.finditer(text)]
    out += [m.group("val").strip() for m in HTML_HREF_RE.finditer(text)]
    return out

def check_internal(from_file: Path, root: Path, target: str) -> bool:
    t = normalize_slashes(strip_angle(target))
    base, _ = split_anchor(t)
    if not base or is_url(base):
        return True
    if base.startswith("/"):
        base = base.lstrip("/")
    p = (from_file.parent / base).resolve()
    if p.exists():
        return True
    p2 = (root / base).resolve()
    if p2.exists():
        return True
    if (root / base / "README.md").exists():
        return True
    if Path(base).suffix == "" and (root / (base + ".md")).exists():
        return True
    return False

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-backup", action="store_true")
    ap.add_argument("--report", default="broken_links_report.txt")
    ap.add_argument("--map", nargs="*", default=[])
    ap.add_argument("--repo", default=None, help='e.g. "https://github.com/ORG/REPO"')
    ap.add_argument("--branch", default=None, help='e.g. "main"')
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    pmap = default_prefix_map()
    for item in args.map:
        k, v = item.split(":", 1)
        pmap[k] = v

    repo = parse_repo(args.repo)

    files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in MD_EXTS]
    changed_files = 0

    for f in files:
        original = f.read_text(encoding="utf-8", errors="replace")
        text = clean_text(original)
        text, nchanges = rewrite_links(text, pmap, repo, args.branch)
        if text != original:
            changed_files += 1
            if not args.dry_run:
                if not args.no_backup:
                    bak = f.with_suffix(f.suffix + ".bak")
                    if not bak.exists():
                        bak.write_text(original, encoding="utf-8")
                f.write_text(text, encoding="utf-8")

    broken = []
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace") if not args.dry_run else clean_text(f.read_text(encoding="utf-8", errors="replace"))
        for t in collect_targets(text):
            if not check_internal(f, root, t):
                broken.append((f, t))

    report_path = root / args.report
    lines = ["Broken internal links report", f"Root: {root}", ""]
    if not broken:
        lines.append("No broken internal links detected.")
    else:
        lines.append(f"Broken links ({len(broken)}):")
        for f, t in broken:
            lines.append(f"- {f.relative_to(root)} -> {t}")
    if not args.dry_run:
        report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Processed {len(files)} files. Changed {changed_files}.")
    print(f"{'(dry-run) Report would be written to:' if args.dry_run else 'Report written to:'} {report_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
