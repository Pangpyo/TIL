CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

INSERT INTO students VALUES
(1, '김광표'), 
(2, '김철수'),
(3, '이호영'),
(4, '박민희'),
(5, '최혜영');

DELETE FROM students WHERE rowid=5;
INSERT INTO students (name) VALUES ('홍길동');
SELECT * FROM students;
-- id	name
-- 1	김광표
-- 2	김철수
-- 3	이호영
-- 4	박민희
-- 6	홍길동

