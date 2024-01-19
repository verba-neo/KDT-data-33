-- 12_distinct.sql
-- 조회 결과 정제

SELECT author_lname FROM books;
SELECT DISTINCT author_lname FROM books;

SELECT released_year FROM books;
SELECT DISTINCT released_year FROM books;

SELECT DISTINCT author_lname, author_fname FROM books;
