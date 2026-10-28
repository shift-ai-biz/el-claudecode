# 3-3 権限設定ワーク

## 準備

このフォルダで一度だけ実行してください。

```bash
pnpm install
```

## ワークの流れ

1. `.claude/settings.json` を作成する（内容は `settings.sample.json` と同じ）
2. 「testディレクトリのadd.jsをpnpmでテストして」→ **allow**: 承認なしで即実行される
3. 「test内のadd.jsを削除して」→ **deny**: 実行が拒否される
4. 「この変更をpushして」→ **ask**: 実行してよいかの確認ダイアログが出る

`deny` は `rm` と `del` の両方を入れてあるので、Windows・macOS のどちらでも同じ挙動になります。
