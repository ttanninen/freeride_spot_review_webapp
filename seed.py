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


def add_dummy_users(i):
    con = get_connection()
    cur =  con.cursor()
    password_hash = "test"
    users = [(f"user_{k}", password_hash) for k in range(1, i + 1)]
    sql = "INSERT INTO users (username, password_hash, added_at) VALUES (?, ?, datetime('now'))"
    cur.executemany(sql, users)
    con.commit()
    con.close()
    return print("database.db populated with example user data")

def add_dummy_spots(i, user_count):
    con = get_connection()
    cur = con.cursor()
    spots = []

    for _ in range(i):
        user_id = random.randint(1, user_count)
        country_id = 115
        continent_id = 3
        title = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 8)))
        max_incline = random.randint(0, 90)
        skill_level_id = random.randint(1, 5)
        aspect = "N"
        notes = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(5, 1000)))
        spots.append((user_id, country_id, continent_id, title, max_incline, skill_level_id, aspect, notes))
        sql = ("""INSERT INTO spots (user_id, country_id, continent_id, title, max_incline, skill_level_id, aspect, notes, added_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """)
        cur.executemany(sql, spots)
    con.commit()
    con.close()
    return print("database.db populated with example spot data")


def add_dummy_messages(i, user_count, spot_count):
    con = get_connection()
    cur = con.cursor()
    messages = []

    for _ in range(i):
        user_id = random.randint(1, user_count)
        spot_id = random.randint(1, spot_count)
        content = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(1, 500)))
        messages.append((user_id, spot_id, content))
        sql = """INSERT INTO messages (user_id, spot_id, content, sent_at) VALUES (?, ?, ?, datetime('now'))"""
        cur.executemany(sql, messages)
    con.commit()
    con.close()
    return print("database.db populated with example message data")


n_users = 1000
n_spots = 2000
n_messages = 400

add_dummy_users(n_users)
add_dummy_spots(n_spots, n_users)
add_dummy_messages(n_messages, n_users, n_spots)

db.commit()
db.close()