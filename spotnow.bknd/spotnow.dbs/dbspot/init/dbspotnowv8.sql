-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dbspotnowv8
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbspotnowv8
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbspotnowv8` DEFAULT CHARACTER SET latin1 ;
USE `dbspotnowv8` ;

-- -----------------------------------------------------
-- Table `dbspotnowv8`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`auth_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`Client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`Client` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nif` VARCHAR(255) NOT NULL,
  `telephone` VARCHAR(45) NOT NULL,
  `user_id` INT(11) NOT NULL,
  `createdDate` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id` (`user_id` ASC),
  CONSTRAINT `Client_user_id_70927fbc_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`Owner`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`Owner` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nif` INT(11) NULL DEFAULT NULL,
  `createdDate` DATETIME(6) NOT NULL,
  `telephone` VARCHAR(45) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id` (`user_id` ASC),
  CONSTRAINT `Owner_user_id_d1ec8cce_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`garage`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`garage` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `isInactive` TINYINT(1) NULL DEFAULT NULL,
  `createdDate` DATETIME(6) NOT NULL,
  `address` VARCHAR(45) NULL DEFAULT NULL,
  `country` VARCHAR(45) NULL DEFAULT NULL,
  `city` VARCHAR(45) NULL DEFAULT NULL,
  `zipcode` VARCHAR(45) NULL DEFAULT NULL,
  `Owner_id` INT(11) NOT NULL,
  `imagem` VARCHAR(100) NULL DEFAULT NULL,
  `Preco` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `garage_Owner_id_740e26d8_fk_Owner_id` (`Owner_id` ASC),
  CONSTRAINT `garage_Owner_id_740e26d8_fk_Owner_id`
    FOREIGN KEY (`Owner_id`)
    REFERENCES `dbspotnowv8`.`Owner` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`Horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`Horario` (
  `idHorario` INT(11) NOT NULL AUTO_INCREMENT,
  `Dia_Semana` VARCHAR(255) NULL DEFAULT NULL,
  `Hora_Inicio` VARCHAR(255) NULL DEFAULT NULL,
  `Hora_Final` VARCHAR(255) NULL DEFAULT NULL,
  `tipo_mensalidade` VARCHAR(255) NULL DEFAULT NULL,
  `garage_id` INT(11) NOT NULL,
  `Preco` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`idHorario`),
  INDEX `Horario_garage_id_38d5f6d7_fk_garage_id` (`garage_id` ASC),
  CONSTRAINT `Horario_garage_id_38d5f6d7_fk_garage_id`
    FOREIGN KEY (`garage_id`)
    REFERENCES `dbspotnowv8`.`garage` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`account_emailaddress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`account_emailaddress` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(254) NOT NULL,
  `verified` TINYINT(1) NOT NULL,
  `primary` TINYINT(1) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email` (`email` ASC),
  INDEX `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id` ASC),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`account_emailconfirmation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`account_emailconfirmation` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created` DATETIME(6) NOT NULL,
  `sent` DATETIME(6) NULL DEFAULT NULL,
  `key` VARCHAR(64) NOT NULL,
  `email_address_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `key` (`key` ASC),
  INDEX `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id` ASC),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e`
    FOREIGN KEY (`email_address_id`)
    REFERENCES `dbspotnowv8`.`account_emailaddress` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`auth_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`django_content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`auth_permission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT(11) NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `dbspotnowv8`.`django_content_type` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`auth_group_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `group_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC),
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `dbspotnowv8`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `dbspotnowv8`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`auth_user_groups` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `group_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC),
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `dbspotnowv8`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`auth_user_user_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC),
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `dbspotnowv8`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`authtoken_token`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`authtoken_token` (
  `key` VARCHAR(40) NOT NULL,
  `created` DATETIME(6) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE INDEX `user_id` (`user_id` ASC),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`booking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`booking` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `state` LONGTEXT NULL DEFAULT NULL,
  `profit` DOUBLE NULL DEFAULT NULL,
  `createdDate` DATETIME(6) NOT NULL,
  `token` VARCHAR(255) NOT NULL,
  `garage_id` INT(11) NOT NULL,
  `Receipt_id` INT(11) NOT NULL,
  `enddate` DATETIME(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `booking_garage_id_dd469876_fk_garage_id` (`garage_id` ASC),
  INDEX `booking_Receipt_id_ea50bbfd_fk_Client_id` (`Receipt_id` ASC),
  CONSTRAINT `booking_Receipt_id_ea50bbfd_fk_Client_id`
    FOREIGN KEY (`Receipt_id`)
    REFERENCES `dbspotnowv8`.`Client` (`id`),
  CONSTRAINT `booking_garage_id_dd469876_fk_garage_id`
    FOREIGN KEY (`garage_id`)
    REFERENCES `dbspotnowv8`.`garage` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`comentario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`comentario` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `comentario` VARCHAR(255) NOT NULL,
  `rating` INT(11) NOT NULL,
  `booking_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `comentario_booking_id_50379a29_fk_booking_id` (`booking_id` ASC),
  CONSTRAINT `comentario_booking_id_50379a29_fk_booking_id`
    FOREIGN KEY (`booking_id`)
    REFERENCES `dbspotnowv8`.`booking` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`django_admin_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT(5) UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) ,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) ,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `dbspotnowv8`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`django_migrations` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`django_site`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`django_site` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `domain` VARCHAR(100) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_site_domain_a2e37b91_uniq` (`domain` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`smartlock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`smartlock` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `IsInactive` TINYINT(1) NULL DEFAULT NULL,
  `createdDate` DATETIME(6) NOT NULL,
  `tokenprimarykey` VARCHAR(255) NULL DEFAULT NULL,
  `garage_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `smartlock_garage_id_0d39a034_fk_garage_id` (`garage_id` ASC),
  CONSTRAINT `smartlock_garage_id_0d39a034_fk_garage_id`
    FOREIGN KEY (`garage_id`)
    REFERENCES `dbspotnowv8`.`garage` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`socialaccount_socialaccount`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`socialaccount_socialaccount` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `provider` VARCHAR(30) NOT NULL,
  `uid` VARCHAR(191) NOT NULL,
  `last_login` DATETIME(6) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  `extra_data` LONGTEXT NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider` ASC, `uid` ASC),
  INDEX `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id` ASC),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `dbspotnowv8`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`socialaccount_socialapp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`socialaccount_socialapp` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `provider` VARCHAR(30) NOT NULL,
  `name` VARCHAR(40) NOT NULL,
  `client_id` VARCHAR(191) NOT NULL,
  `secret` VARCHAR(191) NOT NULL,
  `key` VARCHAR(191) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`socialaccount_socialapp_sites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`socialaccount_socialapp_sites` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `socialapp_id` INT(11) NOT NULL,
  `site_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id` ASC, `site_id` ASC),
  INDEX `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id` ASC),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc`
    FOREIGN KEY (`socialapp_id`)
    REFERENCES `dbspotnowv8`.`socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id`
    FOREIGN KEY (`site_id`)
    REFERENCES `dbspotnowv8`.`django_site` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`socialaccount_socialtoken`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`socialaccount_socialtoken` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `token` LONGTEXT NOT NULL,
  `token_secret` LONGTEXT NOT NULL,
  `expires_at` DATETIME(6) NULL DEFAULT NULL,
  `account_id` INT(11) NOT NULL,
  `app_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id` ASC, `account_id` ASC),
  INDEX `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id` ASC),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc`
    FOREIGN KEY (`account_id`)
    REFERENCES `dbspotnowv8`.`socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc`
    FOREIGN KEY (`app_id`)
    REFERENCES `dbspotnowv8`.`socialaccount_socialapp` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbspotnowv8`.`transaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbspotnowv8`.`transaction` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `amount` DOUBLE NULL DEFAULT NULL,
  `timestamp` DATETIME(6) NULL DEFAULT NULL,
  `createdDate` DATETIME(6) NOT NULL,
  `tipo_transaçao` VARCHAR(45) NOT NULL,
  `booking_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `transaction_booking_id_7c43ce7e_fk_booking_id` (`booking_id` ASC),
  CONSTRAINT `transaction_booking_id_7c43ce7e_fk_booking_id`
    FOREIGN KEY (`booking_id`)
    REFERENCES `dbspotnowv8`.`booking` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
