CREATE TABLE `car_big_data`.`user_table` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(64) NOT NULL NULL,
  `user_password` VARCHAR(64) NOT NULL NULL,
  `user_status` int DEFAULT 0,
  PRIMARY KEY (`id`));