SELECT MAX(num) AS num FROM (
    SELECT num, COUNT(num) FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)t;
