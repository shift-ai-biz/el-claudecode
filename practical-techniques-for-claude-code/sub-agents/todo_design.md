# Todo アプリ技術設計

## 主要機能

### 1. Todo 作成 (CREATE)

-   入力: `{ "title": "string" }`
-   処理: ID とタイムスタンプを自動生成
-   出力: 作成された Todo 項目

### 2. Todo 一覧取得 (READ)

-   入力: なし (またはフィルター条件)
-   出力: Todo 配列

### 3. Todo 更新 (UPDATE)

-   入力: `{ "id": "string", "title"?: "string", "completed"?: "boolean" }`
-   処理: updatedAt を更新
-   出力: 更新された Todo 項目

### 4. Todo 削除 (DELETE)

-   入力: `{ "id": "string" }`
-   出力: 削除成功/失敗

## ファイル構成

```
todo-app/
├── todos.json          # データファイル
├── todo.js             # メイン処理
└── package.json        # 依存関係 (必要に応じて)
```

## エラーハンドリング

-   ファイル読み込み失敗: 空配列で初期化
-   不正な JSON: エラーログを出力して空配列で初期化
-   存在しない ID: null または false を返す
