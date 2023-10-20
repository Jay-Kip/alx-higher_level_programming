-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city` AVG(`value`) AS `avarage_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avarage_temp` DESC;
