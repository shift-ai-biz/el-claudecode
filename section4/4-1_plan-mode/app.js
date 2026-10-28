/**
 * 動作モードの違いを体験するための、ごく小さなサンプル。
 * Manual / Accept Edits の比較では、このファイルに変更を加えます。
 */

function greet(name) {
  return `こんにちは、${name}さん`;
}

function main() {
  console.log(greet("受講者"));
}

main();

module.exports = { greet };
