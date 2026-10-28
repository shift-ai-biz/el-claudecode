"""売上データを集計してレポートを出力するスクリプト。

あえて1つの関数に処理をまとめてあります。
リファクタリングの題材として使ってください。
"""

SALES = [
    {"date": "2026-08-01", "shop": "東京", "item": "ノートPC", "price": 148000, "count": 2},
    {"date": "2026-08-01", "shop": "大阪", "item": "モニター", "price": 32000, "count": 5},
    {"date": "2026-08-02", "shop": "東京", "item": "キーボード", "price": 9800, "count": 12},
    {"date": "2026-08-02", "shop": "名古屋", "item": "ノートPC", "price": 148000, "count": 1},
    {"date": "2026-08-03", "shop": "大阪", "item": "マウス", "price": 4200, "count": 20},
    {"date": "2026-08-03", "shop": "東京", "item": "モニター", "price": 32000, "count": 3},
    {"date": "2026-08-04", "shop": "名古屋", "item": "キーボード", "price": 9800, "count": 7},
]

TAX_RATE = 0.1


def make_report(sales, tax_rate):
    total = 0
    by_shop = {}
    by_item = {}
    for row in sales:
        amount = row["price"] * row["count"]
        total = total + amount
        if row["shop"] in by_shop:
            by_shop[row["shop"]] = by_shop[row["shop"]] + amount
        else:
            by_shop[row["shop"]] = amount
        if row["item"] in by_item:
            by_item[row["item"]] = by_item[row["item"]] + amount
        else:
            by_item[row["item"]] = amount

    lines = []
    lines.append("=== 売上レポート ===")
    lines.append("")
    lines.append("[店舗別]")
    for shop in sorted(by_shop, key=lambda s: by_shop[s], reverse=True):
        lines.append("  " + shop + ": " + f"{by_shop[shop]:,}" + " 円")
    lines.append("")
    lines.append("[商品別]")
    for item in sorted(by_item, key=lambda i: by_item[i], reverse=True):
        lines.append("  " + item + ": " + f"{by_item[item]:,}" + " 円")
    lines.append("")
    lines.append("合計（税抜）: " + f"{total:,}" + " 円")
    lines.append("合計（税込）: " + f"{int(total * (1 + tax_rate)):,}" + " 円")
    return "\n".join(lines)


if __name__ == "__main__":
    print(make_report(SALES, TAX_RATE))
