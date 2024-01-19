-- practice06(CRUD_challenge).sql

-- DB 생성
CREATE DATABASE shirts_db;
USE shirts_db;

-- Table 생성
CREATE TABLE shirts (
	id INT AUTO_INCREMENT PRIMARY KEY,
	article VARCHAR(50) NOT NULL,
    color VARCHAR(50) NOT NULL,
    shirt_size VARCHAR(5) NOT NULL,
    last_worn INT NOT NULL
);
-- Data 입력
INSERT INTO shirts (article, color, shirt_size, last_worn)  
VALUES 
	('t-shirt', 'white', 'S', 10),
	('t-shirt', 'green', 'S', 200),
	('polo shirt', 'black', 'M', 10),
	('tank top', 'blue', 'S', 50),
	('t-shirt', 'pink', 'S', 0),
	('polo shirt', 'red', 'M', 5),
	('tank top', 'white', 'S', 200),
	('tank top', 'blue', 'M', 15);
    
SELECT * FROM shirts;

-- 새로운 데이터 ‘polo shirt’, ‘purlple’, ‘M’, 50 입력
INSERT INTO shirts (article, color, shirt_size, last_worn)
VALUES ('polo shirt', 'purlple', 'M', 50);

-- 모든 셔츠의 `article`과 `color` 만 출력
SELECT article, color FROM shirts;

-- 모든 M 사이즈 셔츠를 출력하되, `id`는 제외
SELECT article, color, shirt_size, last_worn FROM shirts WHERE shirt_size='M';

-- 모든 폴로 셔츠의 사이즈를 L로 변경
UPDATE shirts SET shirt_size='L' WHERE article='polo shirt';

-- `last_worn` 이 15인 셔츠의 `last_worn` 컬럼을 0으로 변경
UPDATE shirts SET last_worn=0 WHERE last_worn=15;

-- 모든 흰색 셔츠의 사이즈를 ‘XS’ 로 바꾸고 색을 ‘off white’ 로 변경
UPDATE shirts SET color='off white', shirt_size='XS' WHERE color='white';

-- `last_worn` 이 200일인 셔츠 모두 삭제
DELETE FROM shirts WHERE last_worn=200;

-- 모든 tank_top 삭제
DELETE FROM shirts WHERE article='tank top';

-- 모든 셔츠 삭제
DELETE FROM shirts;

-- 셔츠 테이블 삭제
DROP TABLE shirts;
SHOW TABLES;