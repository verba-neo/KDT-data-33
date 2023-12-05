-- 01_tabel.sql

CREATE TABLE cats (
	name VARCHAR(50),
    age INT
);

-- 현재 DB에 존재하는 모든 테이블을 보여달라
SHOW TABLES;
-- 특정 테이블 설명
DESC cats;
-- 특정 테이블 삭제
DROP TABLE cats;

CREATE TABLE dogs1 (
	name VARCHAR(50),
    breed VARCHAR(50),
    age INT
);

DESC dogs1;






