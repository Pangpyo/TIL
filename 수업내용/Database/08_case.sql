SELECT * FROM healthcare LIMIT 5;

--  Q. gender가 1인 경우는 남자를 gender가 2인 경우에는 여자를 출력하시오.

SELECT id, 
    CASE 
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END '성별'
FROM healthcare
LIMIT 3;

--  Q. 나이에 따라 청소년(~18), 청년(~30), 중장년(~64)로 출력하시오.

SELECT age 나이,
    CASE
        WHEN age <=18 THEN '청소년'
        WHEN age <= 30 THEN '청년'
        WHEN age <= 64 THEN '중장년'
    END '연령층'
FROM healthcare
LIMIT 10;

--  Q. 흡연 정도를 구분해서 출력하시오.

SELECT id,
    CASE 
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
    END '흡연정도'
FROM healthcare
LIMIT 10;

