-- lists all cities contained in the database hbtn_0d_usa.
-- F A R O U Q
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;
