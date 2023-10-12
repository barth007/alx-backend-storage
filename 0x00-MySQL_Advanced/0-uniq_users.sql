-- This scripts create a table called user
-- columns: 
--        id (int)
--        email (varchar)
--        name  (varchar)
DELIMITER $$

CREATE PROCEDURE  create_user()
BEGIN
  DECLARE id INT;
  DECLARE email VARCHAR(255);
  DECLARE name VARCHAR(255);

  SET id = 0;
  SET email = '';
  SET name = '';

  CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    );
 END $$
CALL create_user $$
DELIMITER ;
