-- Lists all records except ones with no names
SELECT * FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
