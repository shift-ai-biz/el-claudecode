"""在庫管理の最小実装。

タスクB（コメント追加）の対象として使います。
"""


class Inventory:
    def __init__(self):
        self._items = {}

    def add(self, name, count):
        if count <= 0:
            raise ValueError("count は1以上にしてください")
        self._items[name] = self._items.get(name, 0) + count
        return self._items[name]

    def remove(self, name, count):
        current = self._items.get(name, 0)
        if count > current:
            raise ValueError("在庫が足りません")
        self._items[name] = current - count
        return self._items[name]

    def count(self, name):
        return self._items.get(name, 0)

    def low_stock(self, threshold=3):
        return [name for name, count in self._items.items() if count <= threshold]
