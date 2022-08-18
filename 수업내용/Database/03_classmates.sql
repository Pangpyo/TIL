CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL , 
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('김광표', 28, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

SELECT * FROM classmates;
-- name	age	address
-- 김광표	28	서울
-- 김철수	30	제주
-- 이호영	26	인천
-- 박민희	29	대구
-- 최혜영	28	전주

SELECT rowid, name FROM classmates;
-- rowid	name
-- 1	김광표
-- 2	김철수
-- 3	이호영
-- 4	박민희
-- 5	최혜영
SELECT rowid, name FROM classmates LIMIT 2 OFFSET 1;
-- rowid	name
-- 2	김철수
-- 3	이호영
SELECT rowid, name, age FROM classmates LIMIT 3 OFFSET 0;
-- rowid	name	age
-- 1	김광표	28
-- 2	김철수	30
-- 3	이호영	26
SELECT * FROM classmates WHERE address='서울';
-- name	age	address
-- 김광표	28	서울
SELECT rowid, name, age FROM classmates WHERE age<29;
-- rowid	name	age
-- 1	김광표	28
-- 3	이호영	26
-- 5	최혜영	28
SELECT DISTINCT age FROM classmates;
-- age
-- 28
-- 30
-- 26
-- 29
SELECT rowid, name FROM classmates;
DELETE FROM classmates WHERE rowid=5;
-- rowid	name
-- 1	김광표
-- 2	김철수
-- 3	이호영
-- 4	박민희
UPDATE classmates SET address='광주' WHERE rowid=1;
SELECT * FROM classmates;
-- name	age	address
-- 김광표	28	광주
-- 김철수	30	제주
-- 이호영	26	인천
-- 박민희	29	대구
SELECT rowid, name FROM classmates LIMIT 100;
-- rowid	name
-- 1	김광표
-- 2	김철수
-- 3	이호영
-- 4	박민희