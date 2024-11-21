-- Lists all records of the table second_table having a name value in my MySQl server.
-- Records are ordered by descending order.

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
