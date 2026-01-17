SELECT class
FROM (
    SELECT class, COUNT(*) AS cnt
    FROM Courses
    GROUP BY class
) t
WHERE cnt >= 5;