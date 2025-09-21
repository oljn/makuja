CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY,
    restaurant_name TEXT UNIQUE,
    restaurant_address TEXT,
    restaurant_description TEXT
);