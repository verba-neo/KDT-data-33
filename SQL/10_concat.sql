-- 10_concat.sql

SELECT CONCAT(title, '!!!') FROM books;

SELECT CONCAT(author_fname, ' ', author_lname) 
AS 'author full name'
FROM books;

SELECT CONCAT('!', 'S', 'Q', 'L');
SELECT CONCAT_WS('!', 'S', 'Q', 'L');

SELECT CONCAT_WS('-', title, author_fname, author_lname)
AS summary 
FROM books;