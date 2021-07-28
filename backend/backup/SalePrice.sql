CREATE TABLE `car_big_data`.`sale_price` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `min_price` DOUBLE DEFAULT 0,
  `max_price` DOUBLE DEFAULT 0,
  PRIMARY KEY (`id`));