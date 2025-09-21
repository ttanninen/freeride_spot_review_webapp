#Populate db with dummy data
import sqlite3
from random import randint

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

def add_dummy_users():
    usernames = ["Lapinmies", "Graig Kelly", "Jake Burton", "Rio Tahara"]
    password_hash = "test"

    for username in usernames:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        execute(sql, [username, password_hash])
    return print("database.db populated with example user data")

def add_dummy_spots():
    areas = ["Europe", "North-America", "South-America", "Asia"]
    countries = ["Finland", "California", "Chile", "Japan"]
    titles = ["Pyhäkuru", "Jackson Hole", "Aconcagua", "Hokkaido dream line"]
    inclines = ["28", "45", "55", "35"]
    skill_levels = ["Intermediate", "Advanced", "Extreme", "Advanced"]
    aspects = ["S", "NW", "SE", "E"]
    notes_list = ["Classic Lapland line. Starts fairly steep and wide avalance exposure cannot be avoided. Best ridden later in season, march-april.",
                "World-renowned for its challenging freeride terrain, offering steep chutes, wide-open bowls, and legendary backcountry access. iconic lines like Corbet’s Couloir and endless tree runs.",
                "Etreme high-altitude adventure on South America’s tallest peak, where conditions are raw and demanding. Only for the most experienced riders seeking a rare, remote descent.",
                "Endless powder fields and perfectly spaced birch forests, capturing the magic of Japan’s legendary snowfall. Playful terrain and deep, consistent snow. Pure winter bliss."]
    for i in range(1, 5):
        user_id = i
        area = areas[i-1]
        country = countries[i-1]
        title = titles[i-1]
        max_incline = inclines[i-1]
        skill_level = skill_levels[i-1]
        aspect = aspects[i-1]
        notes = notes_list[i-1]
        sql = ("""INSERT INTO spots (user_id, area, country, title, max_incline, skill_level, aspect, notes, added_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now')) 
            """)
        execute(sql, [user_id, area, country, title, max_incline, skill_level, aspect, notes])
    return print("database.db populated with example spot data")


def add_dummy_messages():
        
        contents = ["Great spot!", 
                   "Anyone tried to access the southern ridge yet?", 
                   "Went there last year and had a blast",
                   "My favorite line in whole range!",
                   "Never been here, but hopefully in the future.",
                   "Never again.. broke my board the last time I was here.",
                   "The lower tree run is awesome"]
        for message in contents:
            user_id = randint(1,4)
            spot_id = randint(1,4)
            content = message

            sql = """INSERT INTO messages (user_id, spot_id, content, sent_at) VALUES (?, ?, ?, datetime('now'))"""
            execute(sql, [user_id, spot_id, content])

        return print("database.db populated with example message data")


add_dummy_users()
add_dummy_spots()
add_dummy_messages()
