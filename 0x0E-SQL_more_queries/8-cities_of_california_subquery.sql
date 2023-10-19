-- Lists all the cities of califonia that can be found in the database

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states where name = 'California') ORDER BY id ASC;
