-- This scripts list all bands

DELIMITER $$
DROP PROCEDURE IF EXISTS list_bands $$
CREATE PROCEDURE list_bands()
BEGIN
  SELECT band_name, 
  CASE 
    WHEN split IS NOT NULL THEN split - formed
    ELSE 2022 - formed
    END AS lifespan
  FROM metal_bands
  WHERE style LIKE "%Glam rock%";
END$$
DELIMITER ;
CALL list_bands ;
