# 4-4 Hooks ワーク

## 準備

このフォルダで一度だけ実行してください。

```bash
pnpm install
```

## ワークの流れ

`.claude/settings.json` は手で書かず、**やりたいことを言葉で伝えて Claude Code に設定してもらいます**。

1. このフォルダで `claude` を起動し、自然言語で依頼する

   ```text
   ファイルを編集したら毎回 prettier で自動整形されるように、PostToolUse フックを設定して
   ```

   → `.claude/settings.json` にフックの設定が書き込まれる
2. 生成された `.claude/settings.json` を開いて中身を確認する（ここが一番大事）
   - `hooks` の下の `PostToolUse` … イベント名。**いつ走るか**
   - `matcher`（`Edit|Write`）… **どのツールの後に走るか**
   - `hooks[]` の `command` … **実際に実行されるコマンド**（`npx prettier --write .` など）

   ※ 書き方は生成のたびに変わりうるので、実際に開いたファイルを見て確認してください。
   狙いと違っていれば「対象は Edit と Write だけにして」のように言葉で伝えれば直せます。
   答え合わせ用に `settings.sample.json` を置いてあります
3. `/hooks` でフックが登録されていることを確認する
4. 「`src/greeting.js` の greet に、時間帯（朝/昼/夜）に応じた挨拶を追加して」と依頼する
5. 編集の直後に PostToolUse フックが発火し、`npx prettier --write .` が走る
6. `git diff src/greeting.js` で、**整形済み**（ダブルクォート・セミコロン付与・インデント統一）に
   なっていることを確認する

フックが発火して prettier の整形結果が `git diff` に出れば、このワークは合格です。

`src/greeting.js` は編集で内容が変わります。撮り直すときは
`git checkout -- src/greeting.js` で未整形の状態に戻してください。
