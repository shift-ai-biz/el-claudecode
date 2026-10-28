/** 2つの数値を足して返す。 */
export function add(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("数値を渡してください");
  }
  return a + b;
}

/** 配列の合計を返す。 */
export function sum(values) {
  return values.reduce((total, value) => add(total, value), 0);
}
