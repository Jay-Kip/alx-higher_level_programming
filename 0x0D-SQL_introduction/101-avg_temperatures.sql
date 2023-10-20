-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city` AVG(`value`) AS `avarage_temp`)
FROM `temperatures`
ORDER BY `avarage_temp` DESC;
