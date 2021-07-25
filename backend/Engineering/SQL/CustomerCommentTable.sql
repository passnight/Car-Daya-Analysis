CREATE TABLE `car_big_data`.`customer_comment_table` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `car_model` VARCHAR(64) NOT NULL NULL,
  `car_space` INT DEFAULT 0,
  `car_decoration` INT DEFAULT 0,
  `car_control` INT DEFAULT 0,
  `car_confortableness` INT DEFAULT 0,
  `car_appearance` INT DEFAULT 0,
  `car_value_for_money` INT DEFAULT 0,
  PRIMARY KEY (`id`));