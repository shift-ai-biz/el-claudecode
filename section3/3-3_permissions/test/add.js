import { describe, expect, it } from "vitest";

import { add, sum } from "../src/add.js";

describe("add", () => {
  it("2つの数値を足す", () => {
    expect(add(1, 2)).toBe(3);
  });

  it("マイナスの値も扱える", () => {
    expect(add(-4, 1)).toBe(-3);
  });

  it("数値以外はエラーになる", () => {
    expect(() => add("1", 2)).toThrow(TypeError);
  });
});

describe("sum", () => {
  it("配列の合計を返す", () => {
    expect(sum([1, 2, 3, 4])).toBe(10);
  });

  it("空の配列は0になる", () => {
    expect(sum([])).toBe(0);
  });
});
