-- practice01.sql

CREATE DATABASE practice;
USE practice;

-- people 테이블 생성
CREATE TABLE people (
	first_name VARCHAR(20),
    last_name  VARCHAR(20),
    age        INT
);

-- people 테이블 확인
SHOW tables;
DESC people;

-- people 테이블 삭제
DROP TABLE people;

SHOW TABLES;