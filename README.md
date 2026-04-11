# ATLAS Dashboard

日次ATLASの蓄積・検索・閲覧ダッシュボード

🔗 **Live:** https://yutate.github.io/atlas/

---

## セットアップ

### 1. リポジトリ作成

```bash
git init atlas
cd atlas
# このファイル群をコピー
git add .
git commit -m "init"
git remote add origin https://github.com/yutate/atlas.git
git push -u origin main
```

### 2. GitHub Pages 設定

`Settings → Pages → Source: GitHub Actions`

### 3. 毎日のワークフロー

1. ChatGPTでATLAS完成
2. `data/atlas.json` に以下のフォーマットで追記
3. `git add data/atlas.json && git commit -m "ATLAS 2026-04-11" && git push`
4. 自動でダッシュボードが更新される

---

## JSONスキーマ

`data/atlas.json` はエントリの配列です。新しい日は末尾に追加してください。

```json
[
  {
    "date": "2026-04-11",           // YYYY-MM-DD 形式
    "total_articles": 105,          // 総記事数
    "categories": [
      {
        "name": "Marketing",        // カテゴリ名
        "count": 24,                // 記事数
        "is_cross": false,          // 横断カテゴリ（Z世代など）はtrue
        "summary": "...",           // カテゴリ要約テキスト
        "articles": [
          {
            "title": "記事タイトル",
            "url": "https://...",
            "source": "メディア名"
          }
        ]
      }
    ],
    "signals": [
      "Signal 1 のテキスト",
      "Signal 2 のテキスト"
    ],
    "change": "前日との差分テキスト",
    "insight": "総合考察テキスト"
  }
]
```

---

## ディレクトリ構成

```
atlas/
├── data/
│   └── atlas.json          # ← 毎日追記するデータ
├── scripts/
│   ├── build.py            # ビルドスクリプト
│   └── template.html       # ダッシュボードテンプレート
├── dist/
│   └── index.html          # ビルド成果物（自動生成）
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions
```

---

## ローカルビルド（確認用）

```bash
python scripts/build.py
open dist/index.html
```
