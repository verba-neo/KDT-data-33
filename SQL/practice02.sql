-- practice02.sql

USE practice;

-- people 테이블 생성
CREATE TABLE people (
	first_name VARCHAR(20),
    last_name  VARCHAR(20),
    age        INT
);

INSERT INTO people (first_name, last_name, age)
VALUES
	('철수', '김', 20),
    ('영희', '이', 21),
    ('준수', '박', 24);

-- people 테이블 조회
SELECT * FROM people;