-- script that displays the average temperature(Fahrenheit)
-- by city ordered by temperature(descending).
-- import database(db) using `sudo mysql -u username -p db_name < dump_file.sql`
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
