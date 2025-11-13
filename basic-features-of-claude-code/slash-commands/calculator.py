def add(a, b):
    """2つの数を足す"""
    return a + b


def subtract(a, b):
    """2つの数を引く"""
    return a - b


def multiply(a, b):
    """2つの数を掛ける"""
    return a * b


def divide(a, b):
    """2つの数を割る"""
    if b == 0:
        return "エラー: 0で割れません"
    return a / b
