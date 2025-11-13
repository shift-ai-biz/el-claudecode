# .claude/settings.json 設定メモ

1. .claude/settings.json を作成し、allow（例: `pnpm test`）と deny（例: `rm :\*`）を設定する。

2. 「テストを実行して」と依頼すると、確認なしで即座に実行され、作業が中断されない。

3. 「ファイルを削除して」と依頼すると、deny 設定により実行がブロックされる。

例（.claude/settings.json）:

```json
{
    "permissions": {
        "allow": ["Bash(pnpm:*)", "Bash(cd:*)"],
        "deny": [
            "Bash(del:*)",
            "Bash(rm:*)",
            "Bash(rmdir:*)",
            "Bash(unlink:*)"
        ],
        "ask": []
    }
}
```
