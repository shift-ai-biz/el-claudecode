"""旧版の集計処理（互換のために残しているだけで、もう使っていません）。

ファイル参照を付けずに指示すると、Claude Code がこちらに手を付けようとすることがあります。
"""

import csv


def process_old(path):
    f = open(path, encoding="utf-8")
    reader = csv.reader(f)
    next(reader)
    total = 0
    for row in reader:
        total = total + int(row[2])
    f.close()
    return total
