CREATE TABLE `car_big_data`.`sale_info` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `sale_datetime` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `sale_number` INT NULL DEFAULT 0 ,
  `min_price` DOUBLE DEFAULT 0,
  `max_price` DOUBLE DEFAULT 0,
  PRIMARY KEY (`id`));
