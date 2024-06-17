-- Lists all records from the 'second_table' of the 'hbtn_0c_0' database

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;