CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    added_at TEXT
);

CREATE TABLE continents (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE countries (
    id INTEGER PRIMARY KEY,
    name TEXT,
    continent_id INTEGER REFERENCES continents(id),
    UNIQUE (name, continent_id)
);

CREATE TABLE skill_levels (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE spots (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    continent_id INTEGER REFERENCES continents(id),
    country_id INTEGER REFERENCES countries(id),
    title TEXT,
    max_incline INTEGER,
    skill_level_id INTEGER REFERENCES skill_levels(id),
    aspect TEXT,
    notes TEXT,
    added_at TEXT,
    image BLOB
);

create TABLE messages (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    spot_id INTEGER REFERENCES spots(id) ON DELETE CASCADE,
    content TEXT,
    sent_at TEXT,
    edited_at TEXT

);

CREATE INDEX idx_spot_messages ON messages (spot_id);
CREATE INDEX idx_user_messages ON messages (user_id);
CREATE INDEX idx_spot_user_messages ON messages (spot_id, user_id);
CREATE INDEX idx_messages_sent_at ON messages (sent_at DESC);

CREATE INDEX idx_spots_added_at ON spots (added_at DESC);
CREATE INDEX idx_spots_country ON spots (country_id);
CREATE INDEX idx_spots_continent ON spots (continent_id);
CREATE INDEX idx_spots_user ON spots (user_id);
CREATE INDEX idx_spots_skill_level ON spots (skill_level_id);
CREATE INDEX idx_spots_continent_country ON spots (continent_id, country_id);

CREATE INDEX idx_countries_continent ON countries (continent_id);