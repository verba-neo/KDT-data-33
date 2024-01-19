-- 05_primary_key.sql
USE pet_shop;
INSERT INTO dogs4() VALUES (), (), (), ();
SELECT * FROM dogs4;

CREATE TABLE uniq_dogs (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL DEFAULT 'no name',
	age INT NOT NULL DEFAULT 0
);

DESC uniq_dogs;

INSERT INTO uniq_dogs(name, age) 
VALUES ('ally', 2), ('bob', 3), ('charlie', 1);

INSERT INTO uniq_dogs() 
VALUES (), (), ();

-- 자동으로 중복된 데이터는 허용X
INSERT INTO uniq_dogs(id) VALUES (1);