import db

def get_categories():
    sql_continents = "SELECT id, name FROM continents"
    sql_countries = """SELECT
                            c.id AS country_id,
                            c.name AS country_name,
                            c.continent_id,
                            cont.name AS continent_name
                        FROM countries c
                        JOIN continents cont ON c.continent_id = cont.id"""
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
    sql = ("""INSERT INTO spots 
           (user_id, 
           continent_id, 
           country_id, 
           title, 
           max_incline, 
           skill_level_id, 
           aspect, 
           notes, 
           added_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now')) 
        """)
    db.execute(sql, [user_id, continent, country, title, max_incline, skill_level, aspect, notes])
    return db.last_insert_id()

def spot_count(continent=None, country=None, skill_level=None):
    sql = """SELECT COUNT(*)
            FROM spots s
            JOIN continents cont ON s.continent_id = cont.id
            JOIN countries c ON s.country_id = c.id
            JOIN skill_levels skill ON s.skill_level_id = skill.id
            WHERE 1=1"""

    params = []
    
    if continent:
        sql += " AND cont.name = ?"
        params.append(continent)

    if country:
        sql += " AND c.name = ?"
        params.append(country)
    
    if skill_level:
        sql += " AND skill.name = ?"
        params.append(skill_level)
    
    return db.query(sql, params)[0][0]

def get_spots(page, page_size, continent=None, country=None, skill_level=None):
    sql = """SELECT s.id as id,
                    s.user_id AS user_id,
                    u.username AS username,
                    s.continent_id AS continent_id,
                    cont.name AS continent,
                    s.country_id AS country_id,
                    c.name AS country,
                    s.title AS title,
                    s.max_incline AS max_incline, 
                    skill.name AS skill_level, 
                    s.skill_level_id AS skill_level_id,
                    s.aspect AS aspect, 
                    s.notes AS notes, 
                    s.added_at AS added_at
            FROM spots s
            JOIN users u ON s.user_id = u.id 
            JOIN continents cont ON s.continent_id = cont.id 
            JOIN countries c ON s.country_id = c.id
            JOIN skill_levels skill ON s.skill_level_id = skill.id
            WHERE 1=1"""
   
    params = []

    if continent:
        sql += " AND continent = ?"
        params.append(continent)

    if country:
        sql += " AND country = ?"
        params.append(country)
    
    if skill_level:
        sql += " AND skill.name = ?"
        params.append(skill_level)
    

    limit = page_size
    offset = page_size * (page -1)
    params.append(limit)
    params.append(offset)
    sql += " ORDER BY title LIMIT ? OFFSET ?"

    return db.query(sql, params)

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
    WHERE s.user_id = u.id
    AND s.id = ?
    AND s.continent_id = cont.id
    AND s.country_id = c.id
    AND s.skill_level_id = sk.id"""
    result = db.query(sql, [spot_id])
    return result[0] if result else None

def update_spot(continent, country, title, max_incline, skill_level, aspect, notes, spot_id):
    sql = ("""UPDATE spots SET
        continent_id = ?,
        country_id = ?,
        title = ?,
        max_incline = ?,
        skill_level_id = ?, 
        aspect = ?,
        notes = ?
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
    sql = """INSERT INTO messages 
            (user_id, 
            spot_id, 
            content, 
            sent_at) 
            VALUES (?, ?, ?, datetime('now'))"""
    db.execute(sql, [user_id, spot_id, content])

def get_messages(spot_id):
    sql = """SELECT m.id, 
            m.user_id, 
            u.username, 
            m.spot_id, 
            m.content, 
            m.sent_at, 
            m.edited_at, 
            m.edited_at IS NOT NULL AS is_edited
    FROM messages m, users u
    WHERE m.user_id = u.id AND m.spot_id = ?"""
    return db.query(sql, [spot_id])

def get_message(message_id):
    sql = "SELECT id, user_id, spot_id, content, sent_at, edited_at FROM messages where id = ?"
    return db.query(sql, [message_id])[0]

def get_user_messages(user_id):
    sql = """SELECT m.id, 
            m.user_id, 
            m.spot_id, 
            s.title AS spot_title,
            m.content, 
            m.sent_at, 
            m.edited_at
            FROM messages m
            JOIN spots s ON m.spot_id = s.id
            WHERE m.user_id = ?
            ORDER BY m.sent_at"""
    return db.query(sql, [user_id])

def get_user_spots(user_id):
    sql = """SELECT s.id, 
            s.user_id, 
            s.continent_id, 
            con.name AS continent_name,
            s.country_id,
            c.name AS country_name,
            s.title, 
            s.max_incline, 
            s.skill_level_id, 
            s.aspect, 
            s.notes, 
            s.added_at, 
            s.image 
            FROM spots s
            JOIN continents con ON s.continent_id = con.id
            JOIN countries c ON s.country_id = c.id 
            WHERE user_id = ?"""
    return db.query(sql, [user_id])

def update_message(message_id, content):
    sql = """UPDATE messages SET 
            content = ?, 
            edited_at = datetime('now') 
            WHERE id = ?"""
    db.execute(sql, [content, message_id])

def is_edited(message_id):
    sql = """SELECT id, edited_at IS NOT NULL is_edited
            FROM messages
            WHERE id = ?"""
    result = db.query(sql, [message_id])
    return result[0] if result else None


def remove_message(message_id):
    sql = ("DELETE FROM messages WHERE id = ?")
    db.execute(sql, [message_id])

def update_image(spot_id, image):
    sql = "UPDATE spots SET image = ? WHERE id = ?"
    db.execute(sql, [image, spot_id])

def get_image(spot_id):
    sql = "SELECT image FROM spots WHERE id = ?"
    return db.query(sql, [spot_id])[0]["image"]

def get_latest_spots():
    return None

def get_latest_messages():
    return None