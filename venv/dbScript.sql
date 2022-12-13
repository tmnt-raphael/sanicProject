CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    screen_name VARCHAR(32) UNIQUE,
    email VARCHAR(64) UNIQUE
);

CREATE TABLE job_postings (
    id SERIAL PRIMARY KEY,
    poster VARCHAR(32) REFERENCES users(screen_name),
    job_description VARCHAR(16000),
    job_requirements VARCHAR(16000),
    expiration_time TIMESTAMPTZ
);

CREATE TABLE bids (
    id SERIAL PRIMARY KEY,
    job INT REFERENCES job_postings(id),
    price INT
);