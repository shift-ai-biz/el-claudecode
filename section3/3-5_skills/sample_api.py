"""ユーザー情報を扱う簡易APIハンドラ。

レビューの題材として、いくつか改善の余地を残してあります。
"""

import hashlib
import json
import sqlite3

DB_PATH = "users.db"
ADMIN_TOKEN = "admin-token-2026"


def get_connection():
    return sqlite3.connect(DB_PATH)


def find_user(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE name = '" + name + "'")
    row = cur.fetchone()
    conn.close()
    if row == None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2]}


def create_user(name, email, password, token):
    if token != ADMIN_TOKEN:
        return {"error": "forbidden"}
    conn = get_connection()
    cur = conn.cursor()
    hashed = hashlib.md5(password.encode()).hexdigest()
    cur.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, hashed),
    )
    conn.commit()
    conn.close()
    return {"ok": True}


def list_users(page, per_page):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users")
    rows = cur.fetchall()
    conn.close()
    result = []
    for r in rows:
        result.append({"id": r[0], "name": r[1], "email": r[2]})
    start = page * per_page
    end = start + per_page
    return result[start:end]


def handle(request_body):
    data = json.loads(request_body)
    action = data["action"]
    if action == "find":
        return find_user(data["name"])
    elif action == "create":
        return create_user(data["name"], data["email"], data["password"], data["token"])
    elif action == "list":
        return list_users(data["page"], data["per_page"])
    else:
        return {"error": "unknown action"}
