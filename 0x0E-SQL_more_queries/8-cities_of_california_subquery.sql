-- Lists all the cities of califonia that can be found in the database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states where name = 'Califonia') ORDER BY id ASC;
