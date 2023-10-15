-- This script ranks a country origin of bands, ordered by the
-- number of non unique fans

DELIMITER $$
DROP PROCEDURE IF EXISTS order_band$$
CREATE PROCEDURE order_band()
BEGIN
  SELECT origin, fans as nb_fans FROM metal_bands
  ORDER BY fans DESC;
END$$
DELIMITER ;
CALL order_band;
