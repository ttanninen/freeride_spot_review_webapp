from werkzeug.security import check_password_hash, generate_password_hash
import db

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash, added_at) VALUES (?, ?, datetime('now'))"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])

    if len(result) == 1:
        user_id, password_hash = result[0]
        if check_password_hash(password_hash, password):
            return user_id

    return None

def get_user(user_id):
    sql = "SELECT id, username, added_at FROM users u where u.id = ?"
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_users():
    sql = "SELECT id, username, added_at FROM users"
    return db.query(sql)
