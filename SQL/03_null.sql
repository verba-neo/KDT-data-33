-- 03_null.sql

USE pet_shop;
DESC dogs1;
INSERT INTO dogs1() VALUES ();
SELECT * FROM dogs1;

-- New Table
CREATE TABLE dogs2(
	name VARCHAR(20) NOT NULL,
    age INT NOT NULL
);

DESC dogs2;

-- Error 
INSERT INTO dogs2(name) VALUES ('doggy');

INSERT INTO dogs2(name, age) VALUES ('doggy', 3);
SELECT * FROM dogs2;