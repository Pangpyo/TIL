# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;
```

```
COUNT(*)
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2 and va_right >= 2;
```

```
COUNT(*)
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> ```sqlite
> SELECT COUNT(*) FROM healthcare WHERE blood_pressure > 130;
> SELECT COUNT(*) FROM healthcare WHERE weight*10000/(height*height) > 40;
> SELECT COUNT(*) FROM healthcare WHERE blood_pressure > 130 and weight*10000/(height*height) > 40;
> ```
>
> ``` 
> COUNT(*) 
> 322123
> 전체 백만명중 고혈압 위험군은 약 32프로정도이다.
> COUNT(*)
> 603
> 전체 백만명중 bmi지수가 40을 넘는 고도비만군은 603명이다.
> COUNT(*)
> 366
> bmi지수가 40을 넘는 고도비만군 중에서 고혈압 위험군은 366명으로, 전체 고도비만의 60프로에 해당한다. 이로써 고도비만군은 고혈압일 확률이 높다는 것을 알 수 있었다.
> ```
>
> 