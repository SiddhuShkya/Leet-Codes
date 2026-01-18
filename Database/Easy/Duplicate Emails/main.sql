SELECT email AS Email FROM (
    SELECT email, COUNT(*) AS cnt
    FROM Person
    GROUP BY email
    HAVING cnt > 1
) t;