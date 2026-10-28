// アクセスログから月次レポートを組み立てる処理。
// レビューの題材として、いくつか改善の余地を残してあります。

const fs = require("fs");
const path = require("path");

const LOG_DIR = "./logs";

// 対象月のログファイルを1件ずつ読み込む
function loadEntries(fileNames) {
  const entries = [];
  for (const name of fileNames) {
    const raw = fs.readFileSync(path.join(LOG_DIR, name), "utf8");
    for (const line of raw.split("\n")) {
      if (line.trim() === "") {
        continue;
      }
      entries.push(JSON.parse(line));
    }
  }
  return entries;
}

// 同じユーザーが複数の部署に紐づいていないかを調べる
function findDuplicateUsers(entries) {
  const duplicates = [];
  for (let i = 0; i < entries.length; i++) {
    for (let j = 0; j < entries.length; j++) {
      if (i === j) {
        continue;
      }
      if (
        entries[i].userId === entries[j].userId &&
        entries[i].department !== entries[j].department
      ) {
        if (duplicates.indexOf(entries[i].userId) === -1) {
          duplicates.push(entries[i].userId);
        }
      }
    }
  }
  return duplicates;
}

// 指定されたパターンに一致するパスだけを集計する
function countMatchingPaths(entries, pattern) {
  let count = 0;
  for (const entry of entries) {
    const re = new RegExp(pattern);
    if (re.test(entry.path)) {
      count++;
    }
  }
  return count;
}

// 各ユーザーの所属情報を外部APIから引く
async function attachDepartments(entries, fetchDepartment) {
  const enriched = [];
  for (const entry of entries) {
    const department = await fetchDepartment(entry.userId);
    enriched.push(Object.assign({}, entry, { department: department }));
  }
  return enriched;
}

// 直近のアクセスから順に並べたサマリを作る
function buildRecentSummary(entries) {
  const summary = [];
  for (const entry of entries) {
    summary.unshift({
      userId: entry.userId,
      path: entry.path,
      at: entry.timestamp,
    });
  }
  return summary;
}

async function buildMonthlyReport(fileNames, fetchDepartment, pattern) {
  const entries = loadEntries(fileNames);
  const enriched = await attachDepartments(entries, fetchDepartment);
  return {
    total: enriched.length,
    duplicates: findDuplicateUsers(enriched),
    matched: countMatchingPaths(enriched, pattern),
    recent: buildRecentSummary(enriched),
  };
}

module.exports = {
  loadEntries,
  findDuplicateUsers,
  countMatchingPaths,
  attachDepartments,
  buildRecentSummary,
  buildMonthlyReport,
};
