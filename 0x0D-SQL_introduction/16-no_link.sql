-- script that lists all records of second_table
-- displays score and name in descending order
SELECT score, name FROM second_table
WHERE name is NOT NULL ORDER BY score DESC;
