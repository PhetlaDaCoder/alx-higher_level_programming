-- Lists all records in the table second_table with a score >= 10 in MySQL server.
-- Records are ordered by score.

SELECT *
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

