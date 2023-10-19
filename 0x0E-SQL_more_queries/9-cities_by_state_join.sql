-- Lists all cities contaied in the database
SELECT states.id = cities.state_id RIGHT JOIN cities ON cities.id, cities.name, states.name FROM cities ORDER BY cities.id ASC;
