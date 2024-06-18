-- Create a new databse, Creare the user with password, Grant privilege

CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
SELECT CASE WHEN EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2') THEN 'user_0d_2 exists' ELSE 'user_0d_2 doesn’t exist' END;
FLUSH PRIVILEGES;
