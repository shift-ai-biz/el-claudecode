/** 買い物カゴの金額計算。 */

export const TAX_RATE = 0.1;
export const FREE_SHIPPING_THRESHOLD = 10000;
export const SHIPPING_FEE = 550;

/** 明細の小計を返す。 */
export function subtotal(items) {
  return items.reduce((total, item) => total + item.price * item.quantity, 0);
}

/** 送料を返す（小計が閾値以上なら無料）。 */
export function shippingFee(items) {
  return subtotal(items) >= FREE_SHIPPING_THRESHOLD ? 0 : SHIPPING_FEE;
}

/** 税込の合計金額を返す。 */
export function total(items) {
  const amount = subtotal(items) + shippingFee(items);
  return Math.floor(amount * (1 + TAX_RATE));
}
