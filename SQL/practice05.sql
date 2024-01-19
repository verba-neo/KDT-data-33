-- practice05.sql

USE pet_shop;

UPDATE cats SET name='Jack' WHERE name='Jackson';
UPDATE cats SET breed='British Shorthair'
WHERE name='Ringo';
UPDATE cats SET age=12 WHERE breed='Maine Coon';


DELETE FROM cats WHERE age=4;
DELETE FROM cats WHERE cat_id=age;
DELETE FROM cats;