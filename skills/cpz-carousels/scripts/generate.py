#!/usr/bin/env python3
"""Generate carousel HTML files from content definitions.

Usage:
  python generate.py                              # all rounds, all carousels
  python generate.py --round round_1              # one round only
  python generate.py --round round_2 round_3      # multiple rounds
  python generate.py --carousel c07_big_5_lifts c09_habit_stacking  # specific carousels by ID
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from template import build_carousel
from carousels import round_1, round_2, round_3

ALL_ROUNDS = {
    "round_1": round_1.CAROUSELS,
    "round_2": round_2.CAROUSELS,
    "round_3": round_3.CAROUSELS,
}

OUT_DIR = Path(__file__).parent / "html"


def generate(rounds=None, carousel_ids=None):
    OUT_DIR.mkdir(exist_ok=True)
    count = 0
    for round_name, carousels in ALL_ROUNDS.items():
        if rounds and round_name not in rounds:
            continue
        for key, data in carousels.items():
            if carousel_ids and key not in carousel_ids:
                continue
            html = build_carousel(data["slides"], data["meta"])
            out_path = OUT_DIR / f"{key}.html"
            out_path.write_text(html, encoding="utf-8")
            print(f"  ✓ {out_path.name}  ({len(data['slides'])} slides)")
            count += 1
    print(f"\nGenerated {count} carousel(s) → {OUT_DIR}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate carousel HTML files")
    parser.add_argument(
        "--round",
        nargs="+",
        choices=list(ALL_ROUNDS.keys()),
        metavar="ROUND",
        help=f"Generate specific round(s) only. Choices: {', '.join(ALL_ROUNDS.keys())}",
    )
    parser.add_argument(
        "--carousel",
        nargs="+",
        metavar="ID",
        help="Generate specific carousel(s) by ID (e.g. c07_big_5_lifts)",
    )
    args = parser.parse_args()
    generate(rounds=args.round, carousel_ids=args.carousel)
