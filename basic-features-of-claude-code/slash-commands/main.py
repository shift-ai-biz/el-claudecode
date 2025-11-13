#!/usr/bin/env python3
"""
シンプルなデモプログラム
"""

import calculator
import greeter


def main():
    print("=" * 40)
    print("Python デモプログラム")
    print("=" * 40)

    # 挨拶機能のデモ
    print("\n【挨拶機能】")
    name = "太郎"
    print(greeter.say_hello(name))
    print(greeter.get_greeting("morning"))
    print(greeter.get_greeting("evening"))

    # 計算機能のデモ
    print("\n【計算機能】")
    a, b = 10, 3
    print(f"{a} + {b} = {calculator.add(a, b)}")
    print(f"{a} - {b} = {calculator.subtract(a, b)}")
    print(f"{a} × {b} = {calculator.multiply(a, b)}")
    print(f"{a} ÷ {b} = {calculator.divide(a, b):.2f}")

    # ゼロ除算のテスト
    print(f"{a} ÷ 0 = {calculator.divide(a, 0)}")

    print("\n" + "=" * 40)
    print(greeter.say_goodbye(name))


if __name__ == "__main__":
    main()
