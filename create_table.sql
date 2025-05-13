CREATE TABLE cabins (
    id SERIAL PRIMARY KEY,
    number INT UNIQUE NOT NULL
);

CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    cabin_id INT REFERENCES cabins(id),
    user_name VARCHAR(255),
    user_email VARCHAR(255),
    user_phone VARCHAR(20),
    start_time TIMESTAMP,
    end_time TIMESTAMP
);
