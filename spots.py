import db

def get_spot(spot_id):
    sql = """SELECT s.id, s.user_id, u.username, s.country, s.area, s.title, s.max_incline, s.skill_level, s.aspect, s.notes, s.added_at
    FROM spots s, users u
    WHERE s.user_id = u.id AND s.id = ?"""
    result = db.query(sql, [spot_id])
    return result[0] if result else None

def get_spots():
    sql = """SELECT s.id, u.username, s.country, s.area, s.title, s.max_incline, s.skill_level, s.aspect, s.notes, s.user_id, s.added_at
    FROM spots s, users u
    WHERE s.user_id = u.id"""
    return db.query(sql)

def update_spot(area, country, title, max_incline, skill_level, aspect, notes, spot_id):
    sql = ("""UPDATE spots SET
        area = ?, country = ?, title = ?, max_incline = ?, skill_level = ?, aspect = ?, notes = ?
        WHERE id = ?"""
        )
    db.execute(sql, [area, country, title, max_incline, skill_level, aspect, notes, spot_id])

def remove_spot(spot_id):
    sql = ("DELETE FROM spots WHERE id = ?")
    db.execute(sql, [spot_id])

def search(query):
    sql = """SELECT id, title, notes
            FROM spots
            WHERE LOWER(notes) LIKE ? OR LOWER(title) LIKE ?"""
    pattern = f"%{query}%"
    return db.query(sql, [pattern, pattern])


def get_messages(spot_id):
    sql = """SELECT m.id, m.user_id, u.username, m.spot_id, m.content, m.sent_at
    FROM messages m, users u
    WHERE m.user_id = u.id AND m.spot_id = ?"""
    return db.query(sql, [spot_id])

def edit_message():
    return None

def delete_message():
    return None