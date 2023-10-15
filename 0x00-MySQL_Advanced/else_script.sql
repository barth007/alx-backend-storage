DELIMITER $$
CREATE PROCEDURE ElseTest(INOUT user_name VARCHAR(255),IN name_id VARCHAR(225))
BEGIN
DECLARE unname VARCHAR(255);
SELECT `name` INTO unname
FROM amenities
WHERE name_id = name_id;
IF name_id = "421a55f4-7d82-47d9-b54c-a76916479553"
THEN
SET user_name = "Tea Party";
ELSEIF name_id = "421a55f4-7d82-47d9-b54c-a76916479560"
THEN
SET user_name = "Bush Bar";
ELSEIF name_id = "421a55f4-7d82-47d9-b54c-a76916479557"
THEN
SET user_name = "Zoo Tour";
ENDIF;
END $$
-- DELIMITER ;
-- CALL ElseTest(`@A`, "421a55f4-7d82-47d9-b54c-a76916479553");
