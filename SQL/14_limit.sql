-- 14_limit.sql

SELECT * FROM books LIMIT 5;

-- 재고 많은 5개
SELECT * FROM books 
ORDER BY stock_quantity DESC 
LIMIT 5;

-- 페이지네이션
SELECT * FROM books LIMIT 5;
SELECT * FROM books LIMIT 5, 5;
SELECT * FROM books LIMIT 10, 5;
# limit 은 넘어가도 알아서 끝남
SELECT * FROM books LIMIT 10, 100;