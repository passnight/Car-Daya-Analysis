CREATE TABLE `car_big_data`.`purchasing_purpose_table` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `purchase_purpose`TEXT,
  `comment` TEXT,
  `sale_price` INT NULL DEFAULT 0 
  PRIMARY KEY (`id`));