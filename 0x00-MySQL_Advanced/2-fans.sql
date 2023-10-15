-- This script ranks a country origin of bands, ordered by the
-- number of non unique fans

DELIMITER $$
DROP PROCEDURE IF EXISTS order_band$$
CREATE PROCEDURE order_band()
BEGIN
  SELECT origin, SUM(fans) as nb_fans FROM metal_bands
  GROUP BY origin
  ORDER BY nb_fans DESC;
END$$
DELIMITER ;
CALL order_band;
