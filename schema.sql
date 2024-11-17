DROP TABLE messages;
DROP TABLE user_info;
DROP TABLE users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL);

CREATE TABLE user_info (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users, 
    grade INTEGER,  
    efficient INTEGER);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);
