CREATE TABLE `car_big_data`.`car_fuel_table` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `car_energy_type` VARCHAR(64) NOT NULL NULL,
  `car_fuel_consumption_per_hundred_kilo` INT NULL DEFAULT 0 ,
  `car_comprehensive_fuel_consumption` INT NULL DEFAULT 0 
  PRIMARY KEY (`id`));