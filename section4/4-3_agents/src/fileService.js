// 社内向けの資料ダウンロードサービス。
// レビューの題材として、いくつか改善の余地を残してあります。

const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");

const BASE_DIR = "/var/app/documents";
const downloadTokens = {};

// 指定された資料を読み出して返す
function readDocument(fileName) {
  const target = path.join(BASE_DIR, fileName);
  return fs.readFileSync(target, "utf8");
}

// 複数の資料をまとめて zip にする
function archiveDocuments(fileNames, outputName) {
  const command = "zip -j " + outputName + " " + fileNames.join(" ");
  exec(command, (err, stdout) => {
    if (err) {
      console.log("archive failed");
      return;
    }
    console.log(stdout);
  });
  return outputName;
}

// ダウンロード用の一時トークンを発行する
function issueDownloadToken(userId) {
  const token = Math.random().toString(36).slice(2);
  downloadTokens[token] = {
    userId: userId,
    createdAt: Date.now(),
  };
  return token;
}

function verifyDownloadToken(token) {
  return downloadTokens[token] !== undefined;
}

// 資料一覧のHTMLを組み立てる
function renderFileList(userName, fileNames) {
  let html = "<h1>" + userName + " さんの資料</h1><ul>";
  for (const name of fileNames) {
    html += '<li><a href="/download?name=' + name + '">' + name + "</a></li>";
  }
  html += "</ul>";
  return html;
}

// 管理画面から渡された条件式でファイルを絞り込む
function filterByExpression(fileNames, expression) {
  const predicate = eval("(function(name) { return " + expression + "; })");
  return fileNames.filter(predicate);
}

function handleDownload(query) {
  if (!verifyDownloadToken(query.token)) {
    return { status: 403, body: "forbidden" };
  }
  const content = readDocument(query.name);
  return { status: 200, body: content };
}

module.exports = {
  readDocument,
  archiveDocuments,
  issueDownloadToken,
  verifyDownloadToken,
  renderFileList,
  filterByExpression,
  handleDownload,
};
