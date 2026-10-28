import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from storage import TaskStorage


def test_add_and_list(tmp_path):
    storage = TaskStorage(tmp_path / "tasks.json")
    storage.add("最初のタスク")
    tasks = storage.all()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "最初のタスク"
    assert tasks[0]["done"] is False


def test_complete(tmp_path):
    storage = TaskStorage(tmp_path / "tasks.json")
    task = storage.add("完了にするタスク")
    assert storage.complete(task["id"]) is True
    assert storage.all()[0]["done"] is True


def test_complete_missing(tmp_path):
    storage = TaskStorage(tmp_path / "tasks.json")
    assert storage.complete(999) is False
