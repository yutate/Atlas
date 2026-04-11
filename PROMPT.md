# ATLAS JSON出力プロンプト

ChatGPTでATLASが完成したら、会話の最後にこのプロンプトをそのまま貼る。

---

## コピペ用プロンプト

```
今日のATLASを以下のJSONスキーマで出力してください。
コードブロック（```json）で囲んで、他の文章は不要です。

スキーマ：
{
  "date": "YYYY-MM-DD",
  "total_articles": 総記事数（整数）,
  "categories": [
    {
      "name": "カテゴリ名",
      "count": 記事数（整数）,
      "is_cross": false,  // Z世代など横断カテゴリはtrue
      "summary": "カテゴリ要約テキスト（要約セクションの内容）",
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
    "Signal 1のテキスト",
    "Signal 2のテキスト"
  ],
  "change": "前日差分テキスト（Changeセクションの内容）",
  "insight": "総合考察テキスト（総合考察セクションの内容）"
}

注意：
- articlesは各カテゴリに存在する記事を全件含める
- Z世代カテゴリはis_cross: true にする
- dateは今日の日付 YYYY-MM-DD 形式
- JSONのみ出力、説明文不要
```

---

## atlas.jsonへの追記手順

出力されたJSONをコピーして、`data/atlas.json` の配列末尾に追加する。

### Before（既存データが1件の場合）
```json
[
  { "date": "2026-04-10", ... }
]
```

### After（追記後）
```json
[
  { "date": "2026-04-10", ... },
  { "date": "2026-04-11", ... }
]
```

最後のエントリの `}` の後にカンマを追加してから新しいエントリを貼るだけ。

---

## チェックリスト

追記後、pushする前に確認：

- [ ] dateが今日の日付になっているか
- [ ] 配列の最後の `}` の後に `]` があるか（閉じ忘れ注意）
- [ ] カンマの位置がずれていないか

不安な場合はこのコマンドでバリデーション：
```bash
python3 -c "import json; json.load(open('data/atlas.json')); print('OK')"
```
