-- 11_replace.sql

SELECT REPLACE('Hello World', 'Hell', '****');
SELECT REPLACE(title, ' ', '-') AS new_title FROM books;

-- CHAR_LENGTH
SELECT CHAR_LENGTH('Hello World');

SELECT LENGTH('안녕하세요');
SELECT CHAR_LENGTH('안녕하세요');