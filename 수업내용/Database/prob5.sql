.tables
-- albums          employees       invoices        playlists     
-- artists         genres          media_types     tracks        
-- customers       invoice_items   playlist_track

SELECT * from albums;
SELECT * from employees;
SELECT * from invoices;
SELECT * from playlists;
SELECT * from artists;
SELECT * from genres;
SELECT * from media_types;
SELECT * from tracks;
SELECT * from customers;
SELECT * from invoice_items;
SELECT * from playlist_track;

-- 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.

-- | 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

SELECT *
FROM playlist_track A
ORDER BY PlaylistId DESC LIMIT 5;

-- 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요

-- | 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

SELECT B.TrackId, B.Name
FROM tracks B
ORDER BY TrackId LIMIT 5;

-- 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.

SELECT PL.PlaylistId, TR.Name
FROM playlist_track PL JOIN tracks TR
    ON PL.TrackId = TR.TrackId
ORDER BY PL.PlaylistId DESC LIMIT 10;

-- 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 

SELECT PL.PlaylistId, TR.Name
FROM playlist_track PL JOIN tracks TR
    ON PL.TrackId = TR.TrackId
WHERE PL.PlaylistId = 10
ORDER BY TR.Name DESC LIMIT 5;

-- 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의
--  `Name`을 `INNER JOIN`해서 데이터를 출력하세요.

SELECT COUNT(*)
FROM tracks A INNER JOIN artists B
    ON A.Composer = B.Name;

-- 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 
-- 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.

SELECT COUNT(*)
FROM tracks A LEFT JOIN artists B
    ON A.Composer = B.Name;

-- 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.

SELECT COUNT(*)
FROM tracks A INNER JOIN artists B
    ON A.Composer = B.Name;

SELECT COUNT(*)
FROM tracks A LEFT JOIN artists B
    ON A.Composer = B.Name
WHERE ArtistId IS NOT NULL;
-- ArtistId가 NULL인 트랙들이 있기에 차이가 발생한다. 
-- LEFT조인시에도 ArtistId 가NULL인 값들을 제외하면 행의 개수가 같게 나온다.

-- 8. invoice_items 테이블의 데이터를 출력하세요.

SELECT A.InvoiceLineId, A.InvoiceId
FROM invoice_items A
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 9. invoices 테이블의 데이터를 출력하세요.

SELECT A.InvoiceId, A.CustomerId
FROM invoices A
ORDER BY A.InvoiceId LIMIT 5;

-- 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.

SELECT A.InvoiceLineId, B.InvoiceId
FROM invoice_items A JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.

SELECT A.InvoiceId, B.CustomerId
FROM invoices A JOIN customers B
    ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 
-- 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.

SELECT A.InvoiceLineId, B.InvoiceId, C.CustomerId
FROM invoice_items A 
    JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
    JOIN customers C
    ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

-- 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.

SELECT B.CustomerId, COUNT(*) 개수
FROM invoice_items A 
    JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
    JOIN customers C
    ON B.CustomerId = C.CustomerId
GROUP BY B.CustomerId
ORDER BY B.CustomerId LIMIT 5;

-- 14. 각 customer가 주문한 invoices의 개수, CustomerId 기준 내림차순, 5개

SELECT B.CustomerId, COUNT(*) 송장개수
FROM invoices B
    JOIN customers C
    ON B.CustomerId = C.CustomerId
GROUP BY B.CustomerId
ORDER BY B.CustomerId DESC LIMIT 5;

-- 15.  ArtistId, Name, 각 Artist가 낸 tracks의 수 출력, 트랙 수 기준 내림차순, 10개

SELECT A.Name, COUNT(*) "트랙 수"
FROM artists A JOIN tracks B
    ON A.Name = B.Composer
GROUP BY A.Name
ORDER BY "트랙 수" DESC LIMIT 10;

-- 16. 각 나라 Country 별 고객의 수를 내림차순으로 출력하세요. LIMIT 5

SELECT Country, COUNT(*) "고객 수"
FROM customers
GROUP BY Country
ORDER BY "고객 수" DESC LIMIT 5;

-- 17. 각 나라County 별 주문 건수를 건수 기준으로 내림차순으로 출력하세요. LIMIT 10

SELECT Country, COUNT(*) "고객 수"
FROM customers
GROUP BY Country
ORDER BY "고객 수" DESC LIMIT 5;




-- 17-1. 각 나라 County 별 주문한 물건 개수를 개수 기준으로 내림차순으로 출력하세요. LIMIT 10

SELECT Country, COUNT(*) "물건 개수"
FROM invoice_items A 
    JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
    JOIN customers C
    ON B.CustomerId = C.CustomerId
GROUP BY Country
ORDER BY "물건 개수" DESC LIMIT 5;

-- 17-2. 2010년에 주문한 각 나라 Country 별 주문 물건 개수를 개수 기준으로 내림차순으로 출력하세요. LIMIT 10

SELECT Country, COUNT(*) "물건 개수"
FROM invoice_items A 
    JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
    JOIN customers C
    ON B.CustomerId = C.CustomerId
WHERE B.InvoiceDate LIKE '2010%'
GROUP BY Country
ORDER BY "물건 개수" DESC LIMIT 5;
