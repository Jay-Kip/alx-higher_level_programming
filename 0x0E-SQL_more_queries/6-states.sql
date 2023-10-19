-- Creates a database 'hbtn_0d_usa' and a table 'states'
-- Create Database first
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the created database
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL), PRIMARY KEY (id);
