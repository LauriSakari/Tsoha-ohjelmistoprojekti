DROP TABLE booked_times;
DROP TABLE free_times;
DROP TABLE messages;
DROP TABLE user_info;
DROP TABLE users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL
);

CREATE TABLE user_info (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users, 
    grade INTEGER,  
    efficient INTEGER
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

CREATE TABLE free_times (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users,
    date_of_time DATE
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    CONSTRAINT check_time CHECK (start_time < end_time)
);

CREATE TABLE booked_times (
    free_time_id INT REFERENCES free_times,
    user_id INT REFERENCES users
);