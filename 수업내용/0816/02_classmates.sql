--classmates
-- name : TEXT
-- age : INT
-- address : TEXT

CREATE TABLE classmates (
    name TEXT,
    age INT, 
    address TEXT
);

.schema classmates

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;


INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김광표', 28, '광주');

SELECT rowid, * FROM classmates;

DROP TABLE classmates;