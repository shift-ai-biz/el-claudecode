# 3-5 Skills ワーク

`sample_api.py` を題材に、自作のレビューSkillを作ります。
SKILL.md は手で書かず、**やりたいことを言葉で伝えて Claude Code に作ってもらいます**。

1. このフォルダで `claude` を起動し、`/skills` でいま使えるSkillの一覧を確認する。
   `/review` や `/code-review` などのバンドルSkillと重複しない名前として `my-review` に決める
2. そのまま自然言語で依頼する

   ```text
   review-rules.md のレビュー観点を使う Skill を my-review という名前で作って。コードレビューを依頼されたときに自動で使われるようにして。
   ```

   → `.claude/skills/my-review/SKILL.md` が作られる
3. 生成された `.claude/skills/my-review/SKILL.md` を開いて中身を確認する（ここが一番大事）
   - フロントマターの `name` … コマンド名（`/my-review` で呼び出せる）
   - フロントマターの `description` … どんなときに使うSkillか。**自動起動の引き金**になる
   - 本文 … 実行時に Claude に渡されるレビュー観点（`review-rules.md` の内容が反映されているか確認）

   観点が足りなければ「この観点も足して」と言葉で伝えて直せます
4. `/my-review sample_api.py` を実行して、観点別の指摘が返ることを確認する
5. 「このファイルをレビューして」と自然に頼んでも、description をきっかけに
   同じSkillが呼ばれることを確認する

4と5の2点が確認できればこのワークは合格です。

> Skill そのものを設計・改善するための `skill-creator` という公式プラグインもあります。
> プラグインの導入は Section 5 で扱うので、ここでは使いません。
