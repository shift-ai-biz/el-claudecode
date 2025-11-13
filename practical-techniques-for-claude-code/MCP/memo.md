# Playwright MCP サーバー設定

1. Playwright MCP をプロジェクトに追加

```bash
claude mcp add playwright -s project -- npx @playwright/mcp@latest
```

2. Claude Code に対する指示例（example.com にアクセス）

```text
Playwright を使って https://example.com にアクセスし、ページタイトルと主要見出し（h1, h2）を取得してください。
```

3. 取得対象

-   ページタイトル
-   主要見出し: h1, h2

4. 確認方法（MCP 経由でブラウザを起動して情報取得を確認）

-   MCP が起動していることを確認
-   Claude Code の指示を実行し、取得結果（タイトル・h1・h2）をログや出力で確認する
