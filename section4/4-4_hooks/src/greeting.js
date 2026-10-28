// あえて未整形のまま置いています（セミコロンなし・インデント不揃い・シングルクォート）
// PostToolUse フックで prettier が自動実行されると、この見た目が変わります

function greet(name) {
    if(!name) {
  return 'こんにちは'
    }
  return 'こんにちは、' + name + 'さん'
}

function farewell(name){
      return name + 'さん、また明日'
}

module.exports = { greet , farewell }
