DELIMITER $$
DROP PROCEDURE IF EXISTS GetUserName$$
CREATE PROCEDURE `GetUserName`(INOUT user_name varchar(100),
IN user_id varchar(100))
BEGIN
DECLARE uname varchar(100);
SELECT name INTO uname
FROM users
WHERE user_id = user_id;
IF user_id = "1" 
THEN
SET user_name = "Naira Marley";
ELSEIF user_id = "2" 
THEN
SET user_name = "Big Joe";
ELSEIF user_id = "3" 
THEN
SET user_name = "wizzy kid";
END IF;
END $$
