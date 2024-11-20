-- Lists the number of records with the same score in the table second_table in MySQL server.
-- Records are ordered by descending counnt.
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;
