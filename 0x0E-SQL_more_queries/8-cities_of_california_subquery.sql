-- Lists all the cities of califonia that can be found in the database
-- Results are sorted in ascending order
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
