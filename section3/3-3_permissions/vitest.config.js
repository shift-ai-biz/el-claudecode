import { defineConfig } from "vitest/config";

// 教材では test/add.js をそのままテストファイルとして扱う
export default defineConfig({
  test: {
    include: ["test/**/*.js"],
  },
});
