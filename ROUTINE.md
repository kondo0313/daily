# Daily System セットアップガイド

## 必要なもの

| 項目 | 説明 |
|------|------|
| GitHub Gist | データ保存場所 (無料) |
| Gist Token | `gists` スコープのみで OK |
| Anthropic API Key | チャット機能用 (従量課金) |

---

## 1. GitHub Gist を作る

1. https://gist.github.com にアクセス
2. ファイル名: `system-state.json`、内容: `{}` で作成
3. URLの末尾の英数字が **GIST_ID** → メモしておく

---

## 2. GitHub Token を発行する

1. https://github.com/settings/tokens/new
2. スコープ: `gist` にチェック
3. 生成されたトークンをメモ (一度しか表示されない)

---

## 3. system.html を開く

1. `system.html` をブラウザで開く
2. 右上の鍵アイコン入力欄に **ANTHROPIC_API_KEY** を貼り付け
3. ヘッダーの **↓ Pull** ボタンを押す
4. ダイアログに **GIST_ID** と **Gist Token** を入力
5. 以後、変更は 1.2 秒後に自動保存される

---

## 4. 環境変数 (state.py 用)

```bash
export GIST_ID="your_gist_id_here"
export GIST_TOKEN="your_gist_token_here"
```

PowerShell の場合:
```powershell
$env:GIST_ID   = "your_gist_id_here"
$env:GIST_TOKEN = "your_gist_token_here"
```

---

## 5. 夜間ルーティン (claude code routine)

毎日 4:00 AM に下記を実行して翌日のアドバイスを生成:

```bash
python state.py get > /tmp/today.json
# Claude で /tmp/today.json を読んで aiReview フィールドを更新し state.py set で保存
```

Claude Code での自動化例 (`crontab -e`):
```
0 4 * * * cd /path/to/daily && python routine.py
```

---

## 6. state.py の使い方

```bash
# データ取得
python state.py get

# データ更新
python state.py set '{"streaks": {"study": 5}}'
```

---

## データ構造 (system-state.json)

```json
{
  "streaks": { "study": 0, "vega": 0, "video": 0, "pot": 0 },
  "goals": {
    "vega":  { "long": "", "mid": "", "short": "" },
    "video": { "long": "", "mid": "", "short": "" },
    "pot":   { "long": "", "mid": "", "short": "" }
  },
  "dailyLog": {
    "2025-06-01": {
      "tasks": [
        { "id": "vega", "name": "ベガ練習", "fixed": true, "done": false, "memo": "" }
      ],
      "studyType": "ai"
    }
  },
  "aiReview": "今日の振り返り...",
  "chatHistory": []
}
```
