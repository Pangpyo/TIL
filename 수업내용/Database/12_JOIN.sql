.tables
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;
-- Q. 사용자 (users) 와 각각의 역할을 출력하시오

SELECT users.name, role.title
FROM users INNER JOIN role
    ON users.role_id = role.id;

-- Q. staff(2) 사용자(users)를 역할과 함께 출력하시오.

SELECT users.name, role.title
FROM users INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

-- Q. 사용자(users)와 각각의 역할을 이름의 내림차순으로 출력하시오.

SELECT users.name, role.title
FROM users INNER JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;

-- Q. 모든 게시글을 사용자 정보와 함께 출력하시오.

SELECT *
FROM articles LEFT OUTER JOIN users
    ON users.id = articles.user_id;

-- Q. 작성자가 있는 모든 게시글을 사용자 정보와 함께 출력하시오.

SELECT *
FROM articles LEFT OUTER JOIN users
    ON users.id = articles.user_id
WHERE articles.user_id IS NOT NULL;

SELECT *
FROM articles INNER JOIN users
    ON users.id = articles.user_id;

-- Q. 모든 게시글과 모든 사용자 정보를 출력하시오.

SELECT *
FROM articles FULL OUTER JOIN users
    ON users.id = articles.user_id;

-- Q. users와 role의 CROSS JOIN 결과를 출력하시오.

SELECT *
FROM users CROSS JOIN role;

-- 3개의 테이블 조인

SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;