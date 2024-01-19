--  08_update.sql
USE pet_shop;

UPDATE cats SET age=14 WHERE name='Misty';
UPDATE cats SET age=age+1 WHERE name='Misty';

SELECT * FROM cats;

-- WHERE 구문이 없다면?
SELECT * FROM dogs4;
UPDATE dogs4 SET age=100;