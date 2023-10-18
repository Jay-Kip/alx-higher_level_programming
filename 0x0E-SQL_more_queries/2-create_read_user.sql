-- Creates a database called '2-create_read_user.sql' and the user 'user_0d_2'
-- Creating database first
CRAETE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Now creating the user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Now giving SELECT privillage to user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
