import { describe, it, expect } from 'vitest';
import { add, multiply } from './add.js';

describe('add関数のテスト', () => {
    it('2つの正の数を正しく足し算できる', () => {
        expect(add(2, 3)).toBe(5);
    });

    it('負の数も正しく足し算できる', () => {
        expect(add(-1, -2)).toBe(-3);
    });

    it('0を足しても結果が変わらない', () => {
        expect(add(5, 0)).toBe(5);
    });
});

describe('multiply関数のテスト', () => {
    it('2つの正の数を正しく掛け算できる', () => {
        expect(multiply(3, 4)).toBe(12);
    });

    it('0を掛けると0になる', () => {
        expect(multiply(5, 0)).toBe(0);
    });

    it('負の数の掛け算も正しく計算できる', () => {
        expect(multiply(-2, 3)).toBe(-6);
    });
});
