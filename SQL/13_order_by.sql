-- 13_order_by.sql

SELECT id, author_fname, author_lname FROM books;

SELECT id, author_fname, author_lname FROM books 
ORDER BY author_fname;

SELECT * FROM books ORDER BY stock_quantity;
SELECT * FROM books ORDER BY stock_quantity ASC;
SELECT * FROM books ORDER BY stock_quantity DESC;

-- 여러 컬럼 동시 정렬
SELECT author_lname, released_year, title FROM books 
ORDER BY author_lname;

SELECT author_lname, released_year, title FROM books 
ORDER BY author_lname, released_year;

SELECT author_lname, released_year, title FROM books
ORDER BY author_lname, released_year DESC;

SELECT author_lname, released_year, title FROM books
ORDER BY author_lname DESC, released_year DESC;

-- 함수로 만든 가상의 컬럼도 정렬 가능
SELECT id, CONCAT(author_fname, ' ', author_lname) AS fullname 
FROM books 
ORDER BY fullname, id DESC;