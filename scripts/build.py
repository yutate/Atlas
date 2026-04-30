#!/usr/bin/env python3
"""
build.py - ATLASダッシュボード ビルドスクリプト
data/atlas.json → dist/index.html
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "atlas.json"
TEMPLATE_FILE = ROOT / "scripts" / "template.html"
OUTPUT_DIR = ROOT / "dist"
OUTPUT_FILE = OUTPUT_DIR / "index.html"


def load_data():
    if not DATA_FILE.exists():
        print(f"ERROR: {DATA_FILE} が見つかりません", file=sys.stderr)
        sys.exit(1)
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)
    print(f"✓ {len(data)} 日分のデータを読み込みました")
    total_articles = sum(d.get("total_articles", 0) for d in data)
    print(f"  総記事数: {total_articles}")
    return data


def load_template():
    if not TEMPLATE_FILE.exists():
        print(f"ERROR: {TEMPLATE_FILE} が見つかりません", file=sys.stderr)
        sys.exit(1)
    with open(TEMPLATE_FILE, encoding="utf-8") as f:
        return f.read()


def build():
    data = load_data()
    template = load_template()

    # Validate entries
    for i, entry in enumerate(data):
        if "date" not in entry:
            print(f"WARNING: エントリ {i} に date フィールドがありません")
        if "categories" not in entry:
            print(f"WARNING: {entry.get('date', i)} に categories がありません")

    # Inject data
    data_json = json.dumps(data, ensure_ascii=False, indent=2)
    html = template.replace(
        "// DATA_PLACEHOLDER\nconst ATLAS_DATA = [];",
        f"// AUTO-GENERATED — DO NOT EDIT\nconst ATLAS_DATA = {data_json};"
    )

    # Write output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✓ ビルド完了: {OUTPUT_FILE}")


if __name__ == "__main__":
    build()
