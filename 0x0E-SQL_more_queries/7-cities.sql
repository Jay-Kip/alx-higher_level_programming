-- Creates database 'hbtn_0d_usa' and table 'cities'

-- Create database
CREATE DATABASE hbtn_od_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL, name VARCHAR(256),
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id));
