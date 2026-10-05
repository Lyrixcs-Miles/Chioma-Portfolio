#!/usr/bin/env python3
"""
Scans images/portfolio/<category>/ folders and writes
images/portfolio/manifest.json, which js/main.js fetches at page load to
build the Portfolio grid, the homepage teaser, the hero polaroid stack,
and the page-header photo pool.

Usage, from the project root:

    python scripts/build-image-manifest.py

Run this any time you add, remove, or rename a photo in images/portfolio/,
then commit the updated manifest.json alongside your photo changes.

Adding a new category (e.g. "editorial"): just create
images/portfolio/editorial/, drop images in it, and re-run this script —
it picks up the new folder automatically and adds a matching filter pill
and grid tiles. No HTML or JS edits needed.

Captions: by default every image gets an auto-generated caption/alt text
from its filename (e.g. "garden-casual.jpg" -> "Garden casual"). For a
nicer hand-written caption, add an entry to a captions.json file inside
that category folder (see images/portfolio/fashion/captions.json for a
real example):

    {
      "filename.jpg": {
        "caption": "Short caption shown in the lightbox.",
        "alt": "Longer descriptive alt text for screen readers.",
        "wide": true,
        "cropPosition": "82% 6%",
        "order": 0
      }
    }

All five fields are optional. "wide" marks a tile as the larger
contact-sheet frame. If NO image in a category sets "wide" explicitly,
the script auto-assigns one (the first image, then every 5th) for
visual rhythm; as soon as you set "wide" on even one image in a
category, the auto-rule turns off for that whole category and every
other image defaults to not-wide, so your choices aren't mixed with
the automatic ones. "cropPosition" is a CSS object-position value, for
the rare photo that crops badly at the default center position in a
wide/large tile. "order" (lower sorts first; unset photos sort after
every explicitly-ordered one, in filename order) moves a photo ahead
of plain filename order — this is also how you pin a favorite as a
category's "first" photo, which is what the homepage teaser and the
hero polaroid stack pick from.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_DIR = os.path.join(PROJECT_ROOT, "images", "portfolio")
MANIFEST_PATH = os.path.join(PORTFOLIO_DIR, "manifest.json")

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

# Known categories keep their current display order; any new folder is
# appended after these, sorted alphabetically.
PREFERRED_ORDER = ["fashion", "beauty", "lifestyle"]


def natural_sort_key(name):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", name)]


def prettify(filename):
    stem = os.path.splitext(filename)[0]
    stem = re.sub(r"[-_]+\d+$", "", stem)  # drop a trailing "-01" / "_02" counter
    words = re.split(r"[-_]+", stem)
    words = [w for w in words if w]
    return " ".join(words).capitalize() if words else stem


def category_label(category):
    words = re.split(r"[-_]+", category)
    return " ".join(w.capitalize() for w in words if w)


def load_captions(category_dir):
    path = os.path.join(category_dir, "captions.json")
    if not os.path.isfile(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"WARNING: {path} is not valid JSON ({e}) — ignoring it.", file=sys.stderr)
            return {}


def build_category(category, category_dir):
    captions = load_captions(category_dir)
    label = category_label(category)
    files = [
        f for f in os.listdir(category_dir)
        if os.path.isfile(os.path.join(category_dir, f))
        and os.path.splitext(f)[1].lower() in IMAGE_EXTENSIONS
    ]
    files.sort(key=natural_sort_key)

    # An explicit "order" in captions.json jumps a photo ahead of filename
    # order (lower sorts first); unset photos keep their natural relative
    # order among each other. This is what the Portfolio grid, and the
    # "first photo in each category" picks used by the homepage teaser and
    # hero polaroid stack, actually iterate in — so it's also how you pin a
    # favorite as the teaser/hero pick without renaming the file itself.
    files.sort(key=lambda f: captions.get(f, {}).get("order", 9999))

    # If any file in this category sets "wide" explicitly, treat the whole
    # category as manually curated for that field (unset ones default to
    # false) rather than mixing in the auto-rhythm rule below — otherwise
    # an explicit override plus the auto rule can both mark a tile wide
    # and throw off the intended rhythm.
    any_explicit_wide = any(captions.get(f, {}).get("wide") is not None for f in files)

    items = []
    for i, filename in enumerate(files):
        meta = captions.get(filename, {})
        auto = prettify(filename)
        caption = meta.get("caption", f"{label} — {auto}.")
        alt = meta.get("alt", f"{label} photo: {auto}.")
        wide = meta.get("wide")
        if wide is None:
            wide = False if any_explicit_wide else ((i == 0) or (i > 0 and i % 5 == 0))
        entry = {
            "file": filename,
            "src": f"images/portfolio/{category}/{filename}",
            "caption": caption,
            "alt": alt,
            "wide": bool(wide),
        }
        if meta.get("cropPosition"):
            entry["cropPosition"] = meta["cropPosition"]
        items.append(entry)

        unknown_keys = set(meta.keys()) - {"caption", "alt", "wide", "cropPosition", "order"}
        if unknown_keys:
            print(f"WARNING: {category}/captions.json entry for {filename!r} has unknown key(s): {sorted(unknown_keys)}", file=sys.stderr)

    for filename in captions:
        if filename not in files:
            print(f"WARNING: {category}/captions.json references {filename!r}, which doesn't exist in that folder.", file=sys.stderr)

    return items


def main():
    if not os.path.isdir(PORTFOLIO_DIR):
        print(f"ERROR: {PORTFOLIO_DIR} does not exist.", file=sys.stderr)
        sys.exit(1)

    found = sorted(
        d for d in os.listdir(PORTFOLIO_DIR)
        if os.path.isdir(os.path.join(PORTFOLIO_DIR, d)) and not d.startswith(".")
    )

    category_order = [c for c in PREFERRED_ORDER if c in found]
    category_order += sorted(c for c in found if c not in PREFERRED_ORDER)

    categories = {}
    total = 0
    for category in category_order:
        items = build_category(category, os.path.join(PORTFOLIO_DIR, category))
        if not items:
            print(f"NOTE: {category}/ has no images — skipping it (no empty filter pill added).")
            continue
        categories[category] = items
        total += len(items)
        print(f"{category}: {len(items)} image(s)")

    category_order = [c for c in category_order if c in categories]

    manifest = {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "categoryOrder": category_order,
        "categories": categories,
    }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nWrote {MANIFEST_PATH} — {total} image(s) across {len(category_order)} categor{'y' if len(category_order) == 1 else 'ies'}.")
    print("Commit this file alongside your photo changes and push.")


if __name__ == "__main__":
    main()
