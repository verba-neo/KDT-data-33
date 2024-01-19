-- 07_read.sql

USE pet_shop;

SELECT * FROM cats;
SELECT name FROM cats;
SELECT age FROM cats;
SELECT name, breed FROM cats;

SELECT * FROM cats WHERE cat_id=4;

SELECT name FROM cats WHERE age=4;
SELECT name, age FROM cats WHERE age=4;

SELECT * FROM cats WHERE name='Egg';
SELECT * FROM cats WHERE name='egg';
SELECT * FROM cats WHERE name='eGg';

SELECT name AS '이름' FROM cats;
SELECT name AS '이름', age AS '나이' FROM cats;

