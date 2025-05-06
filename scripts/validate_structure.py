#!/usr/bin/env python3
"""
validate_structure.py
---------------------
Static structure validator for the multi‑lingual docs/ tree.

* Checks for duplicate slugs (same filename) inside each language directory.
* Ensures every Markdown file is referenced from navigation‑map.md, unless
  explicitly listed in .navignore.
* Compares the *base* language (default: `en`) with every other language
  directory and reports missing / extra translations **except** for directories
  that are intentionally single‑language only (e.g. ai‑guidance).
* Validates that all .md files contain correct YAML frontmatter (`title`, `layer`).
* Ignores frontmatter validation for files listed in .navignore.

Exit status is **0** when no issues are found; otherwise prints a readable list
of problems and exits with **1** so CI fails fast.
"""

from __future__ import annotations

import sys
import pathlib
import re
from collections import defaultdict
from typing import Dict, List, Set

import frontmatter

# ────────────────────────────────────────────────────────────────────────────────
# Configuration ─ tweak here if your repo layout changes
# ────────────────────────────────────────────────────────────────────────────────

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "docs"
BASE_LANG = "en"  # language that serves as the "translation source"

# Top‑level directories under docs/ that are *single‑language* and therefore
# should be **excluded from translation comparison**.
EXCLUDE_TRANSLATION_LANGS: Set[str] = {"ai-guidance"}

# Regex to capture Markdown link targets – we only care about *.md inside ()
LINK_RE = re.compile(r"\(([^)]+\.md)\)")

REQUIRED_YAML_FIELDS = {"title", "layer"}

# ────────────────────────────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────────────────────────────

def collect_markdown(root: pathlib.Path) -> Dict[pathlib.PurePosixPath, pathlib.Path]:
    """Return mapping of *relative* Posix path → absolute path for *.md files."""
    return {
        pathlib.PurePosixPath(p.relative_to(root).as_posix()): p
        for p in root.rglob("*.md")
    }

def slug(p: pathlib.PurePosixPath) -> str:
    return p.name.lower()

def load_plain_list(file_path: pathlib.Path) -> Set[str]:
    if not file_path.exists():
        return set()
    return {line.strip() for line in file_path.read_text(encoding="utf-8").splitlines() if line.strip()}

# Files that may legitimately be missing from navigation‑map.md
NAV_IGNORE: Set[pathlib.PurePosixPath] = {
    pathlib.PurePosixPath(p) for p in load_plain_list(DOCS_ROOT / ".navignore")
}

# Slugs that should be ignored in the translation comparison step
IGNORE_SLUGS: Set[str] = {s.lower() for s in load_plain_list(DOCS_ROOT / "ignore-slugs.txt")}

def load_nav_map(lang_root: pathlib.Path) -> Set[pathlib.PurePosixPath]:
    nav_file = lang_root / "navigation-map.md"
    if not nav_file.exists():
        return set()
    links: Set[pathlib.PurePosixPath] = set()
    for line in nav_file.read_text(encoding="utf-8").splitlines():
        for match in LINK_RE.findall(line):
            links.add(pathlib.PurePosixPath(match))
    return links

def find_lang_dirs(root: pathlib.Path) -> Dict[str, pathlib.Path]:
    """Return mapping like { 'en': Path('docs/en'), 'ja': Path('docs/ja'), … }"""
    return {p.name: p for p in root.iterdir() if p.is_dir()}

def check_yaml_frontmatter(md_path: pathlib.Path, rel_path: pathlib.PurePosixPath) -> List[str]:
    errors = []
    if rel_path in NAV_IGNORE:
        return errors  # skip YAML check for ignored files
    try:
        with open(md_path, encoding="utf-8") as f:
            post = frontmatter.load(f)
        for field in REQUIRED_YAML_FIELDS:
            if field not in post:
                errors.append(f"{rel_path} is missing YAML field `{field}`")
    except Exception as e:
        errors.append(f"{rel_path} has malformed YAML frontmatter: {e}")
    return errors

# ────────────────────────────────────────────────────────────────────────────────
# Main validation logic
# ────────────────────────────────────────────────────────────────────────────────

def main() -> None:
    errors: List[str] = []

    lang_dirs = find_lang_dirs(DOCS_ROOT)
    files_by_lang = {lang: collect_markdown(path) for lang, path in lang_dirs.items()}

    # Build slug map so we can catch duplicates easily
    slug_map: Dict[str, Dict[str, List[pathlib.PurePosixPath]]] = {
        lang: defaultdict(list) for lang in lang_dirs
    }

    # ── 1. Per‑language checks ────────────────────────────────────────────────
    for lang, files in files_by_lang.items():
        # 1‑A Duplicate slugs inside one language
        for rel in files:
            slug_map[lang][slug(rel)].append(rel)
        for s, lst in slug_map[lang].items():
            if len(lst) > 1:
                errors.append(
                    f"[{lang.upper()}] Duplicate slug '{s}': {', '.join(map(str, lst))}"
                )

        # 1‑B navigation‑map coverage (unless '.navignore' says otherwise)
        nav_links = load_nav_map(lang_dirs[lang])
        for rel, full_path in files.items():
            if rel in NAV_IGNORE:
                continue
            if rel not in nav_links:
                errors.append(f"{rel} is not listed in {lang}/navigation-map.md")

            # 1‑C YAML frontmatter validation
            errors.extend(check_yaml_frontmatter(full_path, rel))

    # ── 2. Translation completeness check ─────────────────────────────────────
    if BASE_LANG not in slug_map:
        errors.append(f"Base language '{BASE_LANG}' is missing")
    else:
        base_slugs = set(slug_map[BASE_LANG])
        for lang, slugs_dict in slug_map.items():
            if lang == BASE_LANG or lang in EXCLUDE_TRANSLATION_LANGS:
                continue  # skip base and intentionally single‑language dirs

            target_slugs = set(slugs_dict)

            # 2‑A Missing in target language
            for s in sorted(base_slugs - target_slugs):
                if s in IGNORE_SLUGS:
                    continue
                errors.append(
                    f"[{BASE_LANG.upper()}→{lang.upper()}] Missing translation for slug '{s}'"
                )

            # 2‑B Extra in target language
            for s in sorted(target_slugs - base_slugs):
                if s in IGNORE_SLUGS:
                    continue
                errors.append(
                    f"[{lang.upper()}→{BASE_LANG.upper()}] Extra slug '{s}' has no base translation"
                )

    # ── 3. Result output ──────────────────────────────────────────────────────
    if errors:
        print("❌ Structure validation failed:")
        print("\n".join(f"  - {e}" for e in errors))
        sys.exit(1)

    print("✅ Documentation structure is valid.")


if __name__ == "__main__":
    main()
