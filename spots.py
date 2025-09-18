import db

def get_spot(spot_id):
    sql = """SELECT s.id, s.country, s.area, s.title, s.max_incline, s.skill_level, s.aspect, s.notes
    FROM spots s
    WHERE s.id = ?"""
    return db.query(sql, [spot_id])

def get_spots():
    sql = """SELECT s.id, s.country, s.area, s.title, s.max_incline, s.skill_level, s.aspect, s.notes
    FROM spots s"""
    return db.query(sql)

def update_spot(user_id, area, country, title, max_incline, skill_level, aspect, notes, spot_id):
    sql = ("""UPDATE spots s, users, u
           SET s.area = ?, s.country = ?, s.title = ?, s.max_incline = ?, s.skill_level = ?, s.aspect = ?, s.notes = ?)
        WHERE s.id = ? AND u.id = user_id"""
        )
    db.execute(sql, [user_id,area, country, title, max_incline, skill_level, aspect, notes, spot_id])

def delete_spot():
    return None


def get_messages():
    return None

def edit_message():
    return None

def delete_message():
    return None