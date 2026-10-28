# Claude Code コース ワーク教材

エンジニア向け Claude Code コースの、各動画の「デモ＆ワーク」で使う教材です。
動画で説明された手順に沿って、該当するフォルダを開いて進めてください。

## 使い方

```bash
git clone https://github.com/shift-ai-biz/el-claudecode.git
```

git を使わない場合は ZIP でダウンロードして展開してください。
以降は、各動画で指定されたフォルダに `cd` してから `claude` を起動します。

## フォルダと動画の対応

| フォルダ | 動画 | ワークの内容 | 事前準備 |
|---|---|---|---|
| `section2/2-2_first-run/` | 2-2 初回起動と基本操作 | `/init` で CLAUDE.md を生成する | なし |
| `section3/3-1_slash-commands/` | 3-1 スラッシュコマンド | `/init` → `/help` → `/status` → `/usage` → `/context` → `/clear` | なし |
| `section3/3-2_memory/` | 3-2 メモリシステム | CLAUDE.md の有無で出力がどう変わるかを比較する | なし |
| `section3/3-3_permissions/` | 3-3 権限設定 | allow・ask・deny の3パターンを体験する | `pnpm install` |
| `section3/3-4_rewind/` | 3-4 checkpointと/rewind | わざと大きな変更を出させてから巻き戻す | なし |
| `section3/3-5_skills/` | 3-5 Skills | 自然言語でレビューSkillを作らせ、生成された SKILL.md を読んで実行する | なし |
| `section4/4-1_plan-mode/` | 4-1 動作モードとPlan mode | モードごとの承認の求められ方を比べる | なし |
| `section4/4-2_prompt/` | 4-2 プロンプトテクニック | `@` によるファイル参照と Esc での停止 | なし |
| `section4/4-3_agents/` | 4-3 サブエージェント | 自然言語で観点の違うレビュー担当を2つ作らせ、生成された定義ファイルを読んで同じコードに並列でぶつける | なし |
| `section4/4-4_hooks/` | 4-4 Hooks | 自然言語で PostToolUse フックを設定させ、生成された settings.json を読んで自動フォーマットを確認する | `pnpm install` |
| `section4/4-5_mcp/` | 4-5 MCP | Playwright MCP サーバーを設定する | ネット接続・`npx` 実行 |
| `section5/5-1_plugins/` | 5-1 プラグインとチーム標準化 | プラグインを導入して手順を記録する | マーケットプレイス接続 |
| `section5/5-2_quality/` | 5-2 品質担保と自動化 | `/code-review` → 修正 → `/verify` → `claude -p` | `pnpm install` |
| `section5/5-3_worktree/` | 5-3 並列開発 | `claude --worktree` で2セッション並列 | git |

各フォルダの `README.md` に、そのワークの手順を書いてあります。

## 動作確認済みの環境

- Node.js 20 以上（`section3/3-3`・`section4/4-4`・`section5/5-2`）
- Python 3.10 以上（`section2/2-2`・`section3/3-4`・`section4/4-2`）
- pnpm 9 以上

## 旧版の教材について

2025年11月公開の旧版コースの教材（`basic-features-of-claude-code/`・`practical-techniques-for-claude-code/`）は、タグ [`v2-20251113`](https://github.com/shift-ai-biz/el-claudecode/tree/v2-20251113) から参照できます。

## 取り扱い

本教材の著作権は株式会社SHIFT AIに帰属します。本教材は受講者向けの配布物です。取り扱いは受講規約に従ってください。**二次利用は禁止**です。
