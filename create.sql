create database djelen CHARACTER SET utf8 COLLATE utf8_general_ci;
create user 'djelen'@'localhost' identified by 'q';
grant all privileges on djelen.* to 'djelen'@'localhost';