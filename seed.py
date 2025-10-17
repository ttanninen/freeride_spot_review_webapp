#Populate db with dummy data
import sqlite3
import random
import string

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    con.execute(sql, params)
    con.commit()
    con.close()

with get_connection() as db:
    #db.execute("PRAGMA foreign_keys = OFF")
    db.execute("DELETE FROM messages")
    db.execute("DELETE FROM spots")
    db.execute("DELETE FROM users")
    db.commit()


def add_dummy_users(i):
    usernames = ["".join(random.choices(string.ascii_letters, k=random.randint(3,8))) for _ in range(i)]
    password_hash = "test"

    for username in usernames:
        sql = "INSERT INTO users (username, password_hash, added_at) VALUES (?, ?, datetime('now'))"
        execute(sql, [username, password_hash])
    return print("database.db populated with example user data")

def add_dummy_spots(i):
    for _ in range(i):
        user_id = random.randint(1, i)
        country_id = 115
        continent_id = 3
        title = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 8)))
        max_incline = random.randint(0, 90)
        skill_level_id = random.randint(1, 5)
        aspect = "N"
        notes = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(5, 1000)))
        sql = ("""INSERT INTO spots (user_id, country_id, continent_id, title, max_incline, skill_level_id, aspect, notes, added_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """)
        execute(sql, [user_id, country_id, continent_id, title, max_incline, skill_level_id, aspect, notes])
    return print("database.db populated with example spot data")


def add_dummy_messages(i):
    for k in range(i):
        user_id = random.randint(1,i)
        spot_id = random.randint(1,i)
        content = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(1, 500)))
        sql = """INSERT INTO messages (user_id, spot_id, content, sent_at) VALUES (?, ?, ?, datetime('now'))"""
        execute(sql, [user_id, spot_id, content])

    return print("database.db populated with example message data")


add_dummy_users(1000)
add_dummy_spots(500)
add_dummy_messages(300)

db.commit()
db.close()