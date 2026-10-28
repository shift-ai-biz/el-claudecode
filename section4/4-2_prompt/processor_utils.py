"""集計処理から使う小さなヘルパー群。"""


def to_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def percentage(part, whole):
    if not whole:
        return 0.0
    return part / whole * 100


def format_yen(amount):
    return f"{amount:,} 円"
