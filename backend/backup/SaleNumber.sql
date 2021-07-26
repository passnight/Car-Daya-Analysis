CREATE TABLE `car_big_data`.`sale_number` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `sale_month` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `sale_number` DOUBLE DEFAULT 0,
  PRIMARY KEY (`id`));