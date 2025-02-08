CREATE TABLE IF NOT EXISTS leagues (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(50),
    logo VARCHAR(255),
    country_name VARCHAR(100),
    country_code VARCHAR(10),
    country_flag VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS fixtures(
    id INT PRIMARY KEY,
    referee VARCHAR(255),
    date TIMESTAMP,
    venue_name VARCHAR(255),
    status VARCHAR(2),
    elapsed INT,
    league_id INT,
    season INT,
    round VARCHAR(255),
    home_id INT,
    away_id INT,
    goals_home INT,
    goals_away INT,
    ht_goals_home INT,
    ht_goals_away INT,
    penalty_home INT,
    penalty_away INT,
    FOREIGN KEY (league_id) REFERENCES leagues(id)
);