CREATE TABLE `car_big_data`.`basic_sale_info_table` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `sale_datetime` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `sale_region` VARCHAR(64) NOT NULL NULL,
  `sale_price` INT NULL DEFAULT 0 
  PRIMARY KEY (`id`));