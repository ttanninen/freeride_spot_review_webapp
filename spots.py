import db

def get_spots():
    sql = """SELECT s.id, s.country, s.area, s.title, s.max_incline, s.skill_level, s.aspect, s.notes
    FROM spots s"""
    return db.query(sql)