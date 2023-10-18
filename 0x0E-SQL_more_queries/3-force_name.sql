-- script that creates table force_name on your MySQL server
-- force_name values: id INT, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
