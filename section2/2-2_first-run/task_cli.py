"""シンプルなタスク管理CLI。

使い方:
    python task_cli.py add "資料を作る"
    python task_cli.py list
    python task_cli.py done 1
"""

import sys

from storage import TaskStorage

USAGE = """usage: python task_cli.py <command> [args]

commands:
  add <title>   タスクを追加する
  list          タスクの一覧を表示する
  done <id>     タスクを完了にする
"""


def main(argv):
    if len(argv) < 2:
        print(USAGE)
        return 1

    storage = TaskStorage("tasks.json")
    command = argv[1]

    if command == "add":
        if len(argv) < 3:
            print("タイトルを指定してください")
            return 1
        task = storage.add(argv[2])
        print(f"追加しました: [{task['id']}] {task['title']}")
        return 0

    if command == "list":
        tasks = storage.all()
        if not tasks:
            print("タスクはありません")
            return 0
        for task in tasks:
            mark = "x" if task["done"] else " "
            print(f"[{mark}] {task['id']}: {task['title']}")
        return 0

    if command == "done":
        if len(argv) < 3:
            print("IDを指定してください")
            return 1
        if storage.complete(int(argv[2])):
            print("完了にしました")
            return 0
        print("該当するタスクが見つかりません")
        return 1

    print(USAGE)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
