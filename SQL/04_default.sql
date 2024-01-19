-- 04_default.sql
USE pet_shop;

CREATE TABLE dogs3 (
	name VARCHAR(20) DEFAULT 'no name',
    age INT DEFAULT 0
);

INSERT INTO dogs3 () VALUES ();
SELECT * FROM dogs3;

-- NOT NULL vs DEFAULT
INSERT INTO dogs3(name) VALUES (NULL);
SELECT * FROM dogs3;

-- NOT NULL & DEFAULT
CREATE TABLE dogs4 (
	name VARCHAR(20) NOT NULL DEFAULT 'no name',
    age INT NOT NULL DEFAULT 0
);

INSERT INTO dogs4 () VALUES ();
INSERT INTO dogs4 (name) VALUES (NULL);