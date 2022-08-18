

-- Q. users에서 각 성(last_name)씨가 몇 명씩 있는지 조회한다면?

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

-- Q. users에서 각 성(last_name)씨별 평균 나이와 몇 명인지 조회한다면?
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

-- Q. users에서 곽씨들의 성명과 나이를 나이순으로 정렬한다면?

SELECT last_name || first_name 성명, age
FROM users
WHERE last_name = '곽'
ORDER BY age DESC;

-- Q. users에서 100명 이상인 성만 조회한다면?

SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;

-- Q. title과 content라는 컬럼을 가진 articles라는 이름의 table을 새롭게 만들어보세요! (두 컬럼 모두 비어 있으면 안되며, rowid를 사용합니다.)

CREATE TABLE articles (
title TEXT NOT NULL, 
content TEXT NOT NULL
);

-- Q. articles 테이블에 값을 추가해보세요! (title은 ‘1번제목’, content는 ‘1번내용’) 

INSERT INTO articles VALUES ('1번제목', '1번내용');
SELECT * FROM articles;

-- 방금 만든 테이블의 이름을 변경해보기

ALTER TABLE articles RENAME TO news;

-- 방금 만든 테이블에 새로운 컬럼을 추가해보자
-- 1. NOT NULL 설정 없이 추가하기

ALTER TABLE news ADD COLUMN creadted_at TEXT;

-- 2. 기본 값(DEFAULT) 설정하기

ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '';

SELECT * FROM news;

