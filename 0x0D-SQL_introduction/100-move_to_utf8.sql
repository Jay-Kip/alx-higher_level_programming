-- converts hbtn_0c_0 database to UTF8

-- First use the table
USE `hbtn_0c_0`

-- Now convert
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
