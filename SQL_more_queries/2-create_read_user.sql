-- Create a new databse, Creare the user with password, Grant privilege

CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

-- Check if user_0d_2 exists
SELECT
    CASE WHEN EXISTS (
        SELECT 1
        FROM mysql.user
        WHERE user = 'user_0d_2' AND host = 'localhost'
    ) THEN 'Correct output: user_0d_2 exists'
    ELSE 'Correct output: user_0d_2 doesn’t exist'
    END AS result