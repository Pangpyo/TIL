
SELECT A.ID, A.NAME, COUNT(B.SCHEDULED_AT)
FROM PLACES A JOIN SCHEDULES B
    ON A.ID = B.PLACE_ID
GROUP BY A.ID
ORDER BY A.ID;