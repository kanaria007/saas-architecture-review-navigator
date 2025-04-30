#!/usr/bin/env python3
"""
validate_structure.py
---------------------
- Scans Markdown files under docs/<lang> dynamically per language
- Detects duplicate slugs (file names) within each language
- Verifies all files are listed in navigation-map.md (unless excluded via .navignore)
- Detects missing translations based on slug matching (excluding those in ignore-slugs.txt)

Exits with code 1 if validation fails.
"""

import sys
import pathlib
import re
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "docs"
LINK_RE = re.compile(r"\(([^)]+\.md)\)")

def collect_markdown(root: pathlib.Path) -> dict:
    return {
        pathlib.PurePosixPath(p.relative_to(root).as_posix()): p
        for p in root.rglob("*.md")
    }

def slug(p: pathlib.PurePosixPath) -> str:
    return p.name.lower()

def load_nav_map(lang_root: pathlib.Path) -> set:
    nav = lang_root / "navigation-map.md"
    if not nav.exists():
        return set()
    links = set()
    for line in nav.read_text(encoding="utf-8").splitlines():
        for match in LINK_RE.findall(line):
            links.add(pathlib.PurePosixPath(match))
    return links

def load_nav_ignore() -> set:
    f = DOCS_ROOT / ".navignore"
    if not f.exists():
        return set()
    return {
        pathlib.PurePosixPath(line.strip())
        for line in f.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }

def load_ignore_slugs() -> set:
    f = DOCS_ROOT / "ignore-slugs.txt"
    if not f.exists():
        return set()
    return {
        line.strip().lower()
        for line in f.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }

def find_lang_dirs(root: pathlib.Path) -> dict:
    return {p.name: p for p in root.iterdir() if p.is_dir()}

def main() -> None:
    errors = []

    nav_ignore = load_nav_ignore()
    ignore_slugs = load_ignore_slugs()

    lang_dirs = find_lang_dirs(DOCS_ROOT)
    files_by_lang = {lang: collect_markdown(path) for lang, path in lang_dirs.items()}
    slug_map = {lang: defaultdict(list) for lang in lang_dirs}

    for lang, files in files_by_lang.items():
        for rel in files:
            slug_map[lang][slug(rel)].append(rel)

        # Duplicate slugs within one language
        for s, lst in slug_map[lang].items():
            if len(lst) > 1:
                joined = ", ".join(map(str, lst))
                errors.append(f"[{lang.upper()}] Duplicate slug '{s}': {joined}")

        # Navigation map check (excluding .navignore files)
        nav_links = load_nav_map(lang_dirs[lang])
        for rel in files:
            if rel in nav_ignore:
                continue
            if rel not in nav_links:
                errors.append(f"{rel} is not listed in {lang}/navigation-map.md")

    # Missing translations (slug-based, ignoring those in ignore-slugs.txt)
    base_lang = "en"
    if base_lang not in slug_map:
        errors.append(f"Base language '{base_lang}' is missing")
    else:
        base_slugs = set(slug_map[base_lang])
        for lang in slug_map:
            if lang == base_lang:
                continue
            target_slugs = set(slug_map[lang])
            for s in sorted(base_slugs - target_slugs):
                if s in ignore_slugs:
                    continue
                errors.append(f"[{base_lang.upper()}→{lang.upper()}] Missing translation for slug '{s}'")
            for s in sorted(target_slugs - base_slugs):
                if s in ignore_slugs:
                    continue
                errors.append(f"[{lang.upper()}→{base_lang.upper()}] Extra slug '{s}' has no base translation")

    if errors:
        print("❌  Structure validation failed:")
        print("\n".join(f"  - {e}" for e in errors))
        sys.exit(1)

    print("✅  Documentation structure is valid.")

if __name__ == "__main__":
    main()
