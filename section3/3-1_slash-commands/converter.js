/**
 * 単位変換ユーティリティ。
 * 長さ・重さ・温度の変換をまとめて提供する。
 */

const LENGTH_TO_METER = {
  mm: 0.001,
  cm: 0.01,
  m: 1,
  km: 1000,
  inch: 0.0254,
  ft: 0.3048,
};

const WEIGHT_TO_GRAM = {
  mg: 0.001,
  g: 1,
  kg: 1000,
  lb: 453.59237,
};

function convertLength(value, from, to) {
  if (!(from in LENGTH_TO_METER) || !(to in LENGTH_TO_METER)) {
    throw new Error(`未対応の単位です: ${from} -> ${to}`);
  }
  return (value * LENGTH_TO_METER[from]) / LENGTH_TO_METER[to];
}

function convertWeight(value, from, to) {
  if (!(from in WEIGHT_TO_GRAM) || !(to in WEIGHT_TO_GRAM)) {
    throw new Error(`未対応の単位です: ${from} -> ${to}`);
  }
  return (value * WEIGHT_TO_GRAM[from]) / WEIGHT_TO_GRAM[to];
}

function celsiusToFahrenheit(celsius) {
  return celsius * 1.8 + 32;
}

function fahrenheitToCelsius(fahrenheit) {
  return (fahrenheit - 32) / 1.8;
}

module.exports = {
  convertLength,
  convertWeight,
  celsiusToFahrenheit,
  fahrenheitToCelsius,
};
