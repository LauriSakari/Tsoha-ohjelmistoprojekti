
DROP TABLE IF EXISTS booked_times;
DROP TABLE IF EXISTS free_times;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL,
    grade INTEGER,  
    efficient INTEGER
    CONSTRAINT check_grade CHECK (grade > 3 AND grade < 10)
    CONSTRAINT efficient_check CHECK (efficient > 1 AND efficient < 3)
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE free_times (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users,
    location_id INT NOT NULL REFERENCES locations,
    date_of_time DATE,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    CONSTRAINT check_time CHECK (start_time < end_time)
);

CREATE TABLE booked_times (
    PRIMARY KEY (free_time_id, user_id),
    free_time_id INT REFERENCES free_times,
    user_id INT REFERENCES users
);

INSERT INTO locations (name) VALUES ('Ristikko');
INSERT INTO locations (name) VALUES ('Salmisaari');