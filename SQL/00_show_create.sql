-- 00_show_create_db.sql
-- SQL 고정 명령어는 대문자로, 내가 만든 이름은 소문자로.
-- 모두 소문자로 적어도 동작은 하나, Rule 을 지키자.
-- 띄어쓰기와 줄 바꿈은 적절히 잘. DB는 띄어쓰기와 줄바꿈 신경 안씀
-- 주석 (comments) 은 '--'
-- 반드시 명령어 끝에는 세미 콜론 (;) 적기

SHOW DATABASES;

-- DB 생성
CREATE DATABASE test;
-- DB 삭제
DROP DATABASE test;

CREATE DATABASE pet_shop;
-- 특정 DB를 사용하겠다.
USE pet_shop;
