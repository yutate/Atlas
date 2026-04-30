#!/usr/bin/env python3
import json, os, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "atlas.json"
TEMPLATE_FILE = ROOT / "scripts" / "template.html"
OUTPUT_DIR = ROOT / "dist"
OUTPUT_FILE = OUTPUT_DIR / "index.html"

def build():
    data = json.load(open(DATA_FILE, encoding="utf-8"))
    template = open(TEMPLATE_FILE, encoding="utf-8").read()
    daily = [d for d in data if d.get('type') != 'monthly']
    print(f"✓ {len(daily)} 日分 + {len(data)-len(daily)} 月次エントリを読み込みました")
    print(f"  総記事数: {sum(sum(len(c.get('articles',[])) for c in d.get('categories',[])) for d in daily)}")
    data_json = json.dumps(data, ensure_ascii=False, indent=2)
    html = template.replace(
        "// DATA_PLACEHOLDER\nconst ATLAS_DATA = [];",
        f"// AUTO-GENERATED\nconst ATLAS_DATA = {data_json};"
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    open(OUTPUT_FILE, "w", encoding="utf-8").write(html)
    print(f"✓ ビルド完了: {OUTPUT_FILE}")

if __name__ == "__main__":
    build()
