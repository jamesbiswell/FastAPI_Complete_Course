DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `hashed_password` varchar(200) DEFAULT NULL,
  `is_active` int(1) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `todos`;

CREATE TABLE `todos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `priority` int(1) DEFAULT NULL,
  `complete` int(1) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE USER 'todoappuser'@'localhost' IDENTIFIED BY 'todoappuser';

GRANT ALL PRIVILEGES ON * . * TO 'todoappuser'@'localhost';

#
# Starting with MySQL 8.0.4, the MySQL team changed the
# default authentication plugin for MySQL server
# from mysql_native_password to caching_sha2_password.
#
# The command below will make the appropriate updates for your user account.
#
# See the MySQL Reference Manual for details:
# https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html
#

ALTER USER 'todoappuser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'todoapppass';