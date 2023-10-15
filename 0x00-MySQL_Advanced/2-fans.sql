-- This script ranks a country origin of bands, ordered by the
-- number of non unique fans

DELIMITER $$
CREATE PROCEDURE order_band()
BEGIN
  SELECT origin, fans FROM metal_bands
  ORDER BY fans DESC;
END$$
DELIMITER ;
CALL order_band;
