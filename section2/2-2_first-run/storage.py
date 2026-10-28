"""タスクの保存と読み込みを担当するモジュール。"""

import json
import os


class TaskStorage:
    def __init__(self, path):
        self.path = path

    def _load(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, encoding="utf-8") as f:
            return json.load(f)

    def _save(self, tasks):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)

    def all(self):
        return self._load()

    def add(self, title):
        tasks = self._load()
        next_id = max((t["id"] for t in tasks), default=0) + 1
        task = {"id": next_id, "title": title, "done": False}
        tasks.append(task)
        self._save(tasks)
        return task

    def complete(self, task_id):
        tasks = self._load()
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                self._save(tasks)
                return True
        return False
