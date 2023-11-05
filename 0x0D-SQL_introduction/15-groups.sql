-- script that lists number of records with the same score in second_table.
-- displays score and it's number of records with label number
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
