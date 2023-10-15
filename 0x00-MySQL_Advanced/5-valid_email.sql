-- This is a trigger that reset an attribute

DELIMITER $$
DROP TRIGGER IF EXISTS reset_email $$
CREATE TRIGGER reset_email 
BEFORE UPDATE 
ON users FOR EACH ROW
  BEGIN
    IF OLD.email != NEW.email THEN
      SET NEW.valid_email = 0;
    END IF;
  END $$
  DELIMITER ;
