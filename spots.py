import db

def get_categories():
    sql_continents = "SELECT id, name FROM continents"
    sql_countries = "SELECT id, name, continent_id FROM countries"
    sql_skill_levels = "SELECT id, name FROM skill_levels"

    continents = db.query(sql_continents)
    countries = db.query(sql_countries)
    skill_levels = db.query(sql_skill_levels)

    return {"continents": continents, "countries": countries, "skill_levels": skill_levels}


def get_country_continent(country_id):
    sql = "SELECT con.id FROM continents con JOIN countries c ON con.id = c.continent_id WHERE c.id = ?"
    result = db.query(sql, [country_id])
    return result[0]["id"] if result else None

def add_spot(user_id, continent, country, title, max_incline, skill_level, aspect, notes):
    sql = ("""INSERT INTO spots (user_id, continent_id, country_id, title, max_incline, skill_level_id, aspect, notes, added_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now')) 
        """)
    db.execute(sql, [user_id, continent, country, title, max_incline, skill_level, aspect, notes])

def get_spot(spot_id):
    sql = """SELECT s.id AS id,
            s.user_id AS user_id, 
            u.username AS username,
            s.continent_id AS continent_id, 
            cont.name AS continent, 
            s.country_id AS country_id, 
            c.name AS country, 
            s.title AS title, 
            s.max_incline AS max_incline, 
            sk.name AS skill_level, 
            s.skill_level_id AS skill_level_id,
            s.aspect AS aspect, 
            s.notes AS notes, 
            s.added_at AS added_at
    FROM spots s, users u, continents cont, countries c, skill_levels sk
    WHERE s.user_id = u.id AND s.id = ? AND s.continent_id = cont.id AND s.country_id = c.id AND s.skill_level_id = sk.id"""
    result = db.query(sql, [spot_id])
    return result[0] if result else None

def get_spots():
    sql = """SELECT s.id as id, 
            s.user_id AS user_id, 
            u.username AS username,
            s.continent_id AS continent_id, 
            cont.name AS continent, 
            s.country_id AS country_id, 
            c.name AS country, 
            s.title AS title, 
            s.max_incline AS max_incline, 
            sk.name AS skill_level, 
            s.skill_level_id AS skill_level_id,
            s.aspect AS aspect, 
            s.notes AS notes, 
            s.added_at AS added_at
    FROM spots s, users u, continents cont, countries c, skill_levels sk
    WHERE s.user_id = u.id AND s.continent_id = cont.id AND s.country_id = c.id AND s.skill_level_id = sk.id"""
    return db.query(sql)

def update_spot(continent, country, title, max_incline, skill_level, aspect, notes, spot_id):
    sql = ("""UPDATE spots SET
        continent_id = ?, country_id = ?, title = ?, max_incline = ?, skill_level_id = ?, aspect = ?, notes = ?
        WHERE id = ?"""
        )
    db.execute(sql, [continent, country, title, max_incline, skill_level, aspect, notes, spot_id])

def remove_spot(spot_id):
    sql = ("DELETE FROM spots WHERE id = ?")
    db.execute(sql, [spot_id])

def search(query):
    sql = """SELECT id, title, notes
            FROM spots
            WHERE LOWER(notes) LIKE ? OR LOWER(title) LIKE ?"""
    pattern = f"%{query}%"
    return db.query(sql, [pattern, pattern])

def post_message(spot_id, user_id, content):
    sql = """INSERT INTO messages (user_id, spot_id, content, sent_at) VALUES (?, ?, ?, datetime('now'))"""
    db.execute(sql, [user_id, spot_id, content])

def get_messages(spot_id):
    sql = """SELECT m.id, m.user_id, u.username, m.spot_id, m.content, m.sent_at
    FROM messages m, users u
    WHERE m.user_id = u.id AND m.spot_id = ?"""
    return db.query(sql, [spot_id])

def get_user_messages(user_id):
    sql = "SELECT id, user_id, spot_id, content, sent_at FROM messages WHERE user_id = ?"
    return db.query(sql, [user_id])

def get_user_spots(user_id):
    sql = "SELECT id, user_id, continent_id, country_id, title, max_incline, skill_level_id, aspect, notes, added_at, image FROM spots WHERE user_id = ?"
    return db.query(sql, [user_id])

def edit_message():
    return None

def delete_message():
    return None