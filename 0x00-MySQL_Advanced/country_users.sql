-- This script creates a table called users

DELIMITER $$
DROP PROCEDURE IF EXISTS create_detail $$

CREATE PROCEDURE create_detail()
BEGIN
  DECLARE id INT;
  DECLARE email VARCHAR(255);
  DECLARE name VARCHAR(255);
  DECLARE country VARCHAR(2);


  SET id = 0;
  SET email = '';
  SET name = '';
  SET country ='US';


  CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN')
    );
END $$
DELIMITER ;
CALL create_detail;
