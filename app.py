import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

get_user("1 OR 1=1")
