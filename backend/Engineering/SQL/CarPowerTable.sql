CREATE TABLE `car_big_data`.`car_power_table` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `car_max_power` INT NULL DEFAULT 0 ,
  `car_max_torque` INT NULL DEFAULT 0 ,
  `car_max_horsepower` INT NULL DEFAULT 0 ,
  `car_max_speed` INT NULL DEFAULT 0 ,
  `car_acceleration` INT NULL DEFAULT 0 
  PRIMARY KEY (`id`));