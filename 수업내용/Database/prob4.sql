
-- 1. 모든 테이블의 이름을 출력하세요.

.tables

-- albums          employees       invoices        playlists     
-- artists         genres          media_types     tracks        
-- customers       invoice_items   playlist_track

-- 2. 모든 테이블의 데이터를 확인해보세요.

SELECT * from albums;
SELECT * from employees;
SELECT * from invoices;
SELECT * from playlists;
SELECT * from artists;
SELECT * from genres;
SELECT * from media_types;
SELECT * from tracks ;
SELECT * from customers;
SELECT * from invoice_items;
SELECT * from playlist_track;

-- 3. 앨범(albums) 테이블의 데이터를 출력하세요.

SELECT * from albums ORDER BY Title DESC LIMIT 5;

-- 4. 고객(customers) 테이블의 행 개수를 출력하세요.

SELECT COUNT(*) '고객 수' from customers;

-- 5. 고객(customers) 테이블에서 고객이 사는 나라가 USA인 고객의 FirstName, LastName을 출력하세요.

SELECT FirstName 이름 , LastName 성 
FROM customers 
WHERE Country = 'USA'
ORDER BY FirstName DESC LIMIT 5;

-- 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.

SELECT COUNT(*) '송장 수'
FROM invoices
WHERE BillingPostalCode NOT NULL;

-- 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.

SELECT *
FROM invoices
WHERE BillingState NOT NULL
ORDER BY InvoiceDate DESC LIMIT 5;

-- 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.

SELECT COUNT(*)
FROM invoices
WHERE InvoiceDate LIKE '2013-%';

SELECT COUNT(*)
FROM invoices
WHERE strftime('%Y',InvoiceDate) = '2013';

-- 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.

SELECT CustomerId 고객ID, FirstName 이름, LastName 성
FROM customers
WHERE FirstName LIKE 'L%';

-- 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.

SELECT COUNT(*) "고객 수", Country '나라'
FROM customers
GROUP BY Country
ORDER BY "고객 수" DESC LIMIT 5;

-- 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

SELECT ArtistId, COUNT(*) "앨범 수"
FROM albums
GROUP BY ArtistId
ORDER BY "앨범 수" DESC LIMIT 1;

-- 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요

SELECT ArtistId, COUNT(*) "앨범 수"
FROM albums
GROUP BY ArtistId
HAVING "앨범 수" >= 10
ORDER BY "앨범 수" DESC;

-- 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 
-- 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.

SELECT COUNT(*) "고객 수", Country, State
FROM customers
WHERE State NOT NULL
GROUP BY Country, State
ORDER BY "고객 수" DESC, State DESC LIMIT 5;

-- 14. 고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.

SELECT CustomerId, 
    CASE 
        WHEN Fax IS NULL THEN 'X'
        WHEN Fax IS NOT NULL THEN 'O'
    END 'Fax 유/무'
FROM customers
ORDER BY CustomerId LIMIT 5;

-- 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.

SELECT LastName, FirstName, strftime('%Y','now')-BirthDate+1 "나이"
FROM employees
ORDER BY EmployeeId;

-- 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.

SELECT Name
FROM artists
WHERE ArtistId = (
    SELECT ArtistId
    FROM albums
    GROUP BY ArtistId
    ORDER BY COUNT(*) DESC LIMIT 1
);

-- 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.

SELECT Name
FROM genres
WHERE GenreId = (
    SELECT GenreId
    FROM tracks
    GROUP BY GenreId
    ORDER BY COUNT(*) LIMIT 1
);
