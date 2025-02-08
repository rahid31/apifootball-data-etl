CREATE TABLE IF NOT EXISTS leagues (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(50),
    logo VARCHAR(255),
    country_name VARCHAR(100),
    country_code VARCHAR(10),
    country_flag VARCHAR(255)
);