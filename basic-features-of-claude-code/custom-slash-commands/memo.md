# Claude によるコードレビューの手順

1. コマンドディレクトリの作成

    - `mkdir -p .claude/commands`

2. コマンドファイルの作成

    - `.claude/commands/review.md` を作成

3. レビュープロンプトの記述

    - レビュー観点を詳細に記述:
        - コード品質
        - 機能性
        - セキュリティ
        - その他必要な観点

4. レビューの実行
    - コード変更後、Claude Code 上で `/project:review` を実行
