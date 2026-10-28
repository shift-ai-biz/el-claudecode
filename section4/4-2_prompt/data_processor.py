"""CSVの売上データを読み込んで集計する処理。

ワークでリファクタリングの対象にするのは **このファイル** です。
"""

import csv


def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def process(path):
    rows = load(path)
    total = 0
    by_category = {}
    errors = []
    for row in rows:
        try:
            amount = int(row["amount"])
        except ValueError:
            errors.append(row)
            continue
        total = total + amount
        category = row["category"]
        if category in by_category:
            by_category[category] = by_category[category] + amount
        else:
            by_category[category] = amount
    summary = {}
    summary["total"] = total
    summary["by_category"] = by_category
    summary["error_count"] = len(errors)
    summary["average"] = total / len(rows) if len(rows) > 0 else 0
    return summary


def print_summary(summary):
    print("合計:", summary["total"])
    print("平均:", round(summary["average"], 1))
    for category in summary["by_category"]:
        print(category, ":", summary["by_category"][category])
    if summary["error_count"] > 0:
        print("読み飛ばした行:", summary["error_count"])


if __name__ == "__main__":
    print_summary(process("sales.csv"))
