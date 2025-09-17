CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE locations (
    id INTEGER PRIMARY KEY,
    area TEXT UNIQUE,
    country TEXT UNIQUE
);

CREATE TABLE spots (
    id INTERGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    country TEXT,
    area TEXT,
    title TEXT,
    skill_level TEXT,
    aspect INTEGER,
    notes TEXT,
    added_at TEXT
);

create TABLE messages (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    spot_id INTEGER REFERENCES spots,
    sent_at TEXT

)