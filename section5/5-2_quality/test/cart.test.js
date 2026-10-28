import { describe, expect, it } from "vitest";

import { shippingFee, subtotal, total } from "../src/cart.js";

const items = [
  { name: "キーボード", price: 9800, quantity: 1 },
  { name: "マウス", price: 4200, quantity: 2 },
];

describe("subtotal", () => {
  it("明細の小計を返す", () => {
    expect(subtotal(items)).toBe(18200);
  });

  it("空のカゴは0円", () => {
    expect(subtotal([])).toBe(0);
  });
});

describe("shippingFee", () => {
  it("1万円以上なら送料無料", () => {
    expect(shippingFee(items)).toBe(0);
  });

  it("1万円未満なら送料がかかる", () => {
    expect(shippingFee([{ name: "マウス", price: 4200, quantity: 1 }])).toBe(550);
  });
});

describe("total", () => {
  it("税込の合計を返す", () => {
    expect(total(items)).toBe(20020);
  });
});
