SELECT * FROM users;

-- Q. users에서 가장 나이가 작은 사람의 수는?

SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);

-- Q. users에서 평균 계좌 잔고보다 높은 사람의 수는?

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- Q. users에서 유은정과 같은 지역에 사는 사람의 수는?

SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE first_name = '은정' AND last_name = '유');

-- Q. 전체 인원과 평균 연봉, 평균 나이를 출력하세요.

SELECT 
    (SELECT COUNT(*) FROM users) '총 인원',
    (SELECT AVG(balance) FROM users) '평균 연봉' ,
    (SELECT AVG(age) FROM users) '평균 나이'
;

-- Q. 단일행 서브쿼리 – UPDATE에서의 활용

UPDATE users
SET balance = (SELECT AVG(balance) FROM users);

-- Q. users에서 이은정과 같은 지역에 사는 사람의 수는?
-- 이은정은 여러명
SELECT COUNT(*)
FROM users
WHERE country IN (
    SELECT country
    FROM users
    WHERE first_name = '은정' AND last_name = '이'
);

-- Q. 특정 성씨에서 가장 어린 사람들의 이름과 나이

SELECT last_name, first_name, age
FROM users
WHERE (last_name, age) IN (
    SELECT last_name, MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;