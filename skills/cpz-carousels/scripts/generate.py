#!/usr/bin/env python3
"""Generate carousel HTML files from a JSON content spec.

Fully dynamic — there is no pre-registered carousel list. Content is
authored as JSON at runtime (by hand, or by an autonomous agent) and
passed directly to this script. See example_carousel.json for the schema,
and template.py's module docstring for the full slide/meta key reference.

JSON shape — either a single carousel:
    {"meta": {...}, "slides": [...]}
or multiple carousels keyed by id:
    {"carousel_id_1": {"meta": {...}, "slides": [...]}, "carousel_id_2": {...}}

Usage:
  python generate.py my_carousel.json                    # -> html/<id>.html
  python generate.py carousel_a.json carousel_b.json      # multiple files
  python generate.py content.json --out /path/to/html/    # custom output dir
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from template import build_carousel


def _load_carousels(json_path: Path) -> dict:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    if "meta" in data and "slides" in data:
        cid = data["meta"].get("id") or json_path.stem
        return {cid: data}
    return data


def generate(json_paths: list[Path], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for json_path in json_paths:
        carousels = _load_carousels(json_path)
        for cid, data in carousels.items():
            html = build_carousel(data["slides"], data["meta"])
            out_path = out_dir / f"{cid}.html"
            out_path.write_text(html, encoding="utf-8")
            print(f"  ✓ {out_path.name}  ({len(data['slides'])} slides)")
            count += 1
    print(f"\nGenerated {count} carousel(s) → {out_dir}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate carousel HTML from a JSON content spec")
    parser.add_argument(
        "json_paths",
        nargs="+",
        type=Path,
        metavar="JSON_FILE",
        help="JSON file(s) with carousel content (single or multi-carousel shape)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).parent / "html",
        metavar="PATH",
        help="Output directory for generated HTML (default: scripts/html/)",
    )
    args = parser.parse_args()
    generate(args.json_paths, args.out)
