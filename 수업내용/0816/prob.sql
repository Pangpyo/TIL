-- 1. 추가되어 있는 모든 데이터의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare;

-- 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE age < 10;

-- 3. 성별이 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE gender = 1;

-- 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;

-- 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.
SELECT DISTINCT sido FROM healthcare;

-- 6. 혈압과 몸무게의 상관관계를 출력해본다.
SELECT COUNT(*) FROM healthcare WHERE blood_pressure > 130;
SELECT COUNT(*) FROM healthcare WHERE weight*10000/(height*height) > 40;
SELECT COUNT(*) FROM healthcare WHERE blood_pressure > 130 and weight*10000/(height*height) > 40;

