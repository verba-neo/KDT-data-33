-- 15_like.sql

-- 정확하지 않으면 검색 안됨
SELECT * FROM books WHERE author_fname='Dav';

-- 정확하지 않더라도 검색 가능
-- % ) 이 자리에는 0개부터 N개까지 들어올 수 있음
-- _ ) 이 자리에는 오직 한 글자만 올 수 있음

-- 이름이 da 로 시작하는 모든 사람
SELECT * FROM books WHERE author_fname LIKE 'da%';
-- 이름에 da가 들어가는 모든사람
SELECT * FROM books WHERE author_fname LIKE '%da%';
-- 책 제목에 어디라도 ':' 이 들어가는 책
SELECT * FROM books WHERE title LIKE '%:%';

-- 'da' 로 시작하고 뒤에 두글자만 있는 사람
SELECT * FROM books WHERE author_fname LIKE 'da__';
-- 이름 4글자 
SELECT * FROM books WHERE author_fname LIKE '____';

-- '%' 특수기호가 들어간 책을 찾으려면?
SELECT * FROM books WHERE title LIKE '%\%%';









