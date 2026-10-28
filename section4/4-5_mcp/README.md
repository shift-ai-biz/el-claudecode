# 4-5 MCP ワーク

`.mcp.json` はあえて置いていません。追加コマンドを打つところから始めます。

```bash
claude mcp add playwright -s project -- npx @playwright/mcp@latest
claude mcp list
```

1. 上のコマンドで Playwright MCP サーバーを **プロジェクトスコープ**で追加する
   （設定はこのフォルダ直下の `.mcp.json` に保存される）
2. `claude mcp list` で状態を確認する → 初回は **Pending approval**
3. `claude` を起動して承認する → **connected** になる
4. `/mcp` で接続状態と提供ツールを確認する
5. 「Playwrightを使って https://example.com にアクセスし、ページタイトルと主要見出しを取得してください」
   と指示する

## 元に戻す

```bash
claude mcp remove playwright -s project
claude mcp reset-project-choices
```

`.mcp.json` も削除すると、未設定の状態から撮り直せます。
