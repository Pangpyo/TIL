-- (성+이름) 출력, 5명만
SELECT 
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;

-- 문자열 길이 LENGTH

SELECT 
    last_name||first_name 이름,
    LENGTH(last_name || first_name) '이름의 길이'
FROM users
LIMIT 5;

-- 이름   이름의 길이
-- ---  ------
-- 유정호  3
-- 이경희  3
-- 구정자  3
-- 장미경  3
-- 차영환  3

-- 문자열 변경 REPLACE

SELECT 
    first_name,
    phone,
    REPLACE(phone, '-', '') '-제거'
FROM users
LIMIT 5;


