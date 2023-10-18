-- script lists all the cities of California that can be found in hbtn_0d_usa
-- Results are sorted in ascending order by cities.id
SELECT cities.id, cities.name 
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
