-- 02_insert_data.sql
USE pet_shop;

INSERT INTO dogs1 (name, breed, age)
VALUES            ('맥스', '말티즈', 4);

-- Error) 컬럼 순서대로 값을 넣어야 함.
INSERT INTO dogs1 (name, breed, age)
VALUES 		      ('소리', 4, '포메');

-- 여러 데이터 한번에 입력 가능
INSERT INTO dogs1 (name, breed, age)
VALUES
	('짱구', '요크셔', 6),
    ('소리', '포메', 3),
    ('가을', '치와와', 1);
    
-- 테이블 데이터 조회
SELECT * FROM dogs1;







