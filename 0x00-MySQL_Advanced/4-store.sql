-- This scripts creates trigger that
-- decreases the quantity of item 
-- after been added

DELIMITER $$
DROP TRIGGER IF EXISTS decrease_item $$
CREATE TRIGGER decrease_item
AFTER INSERT ON orders FOR EACH ROW
BEGIN
  UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END$$
DELIMITER ;
