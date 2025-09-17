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

INSERT INTO locations () 

CREATE TABLE spots (
    id INTERGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    country TEXT REFERENCES locations,
    area TEXT REFERENCES locations,
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

);