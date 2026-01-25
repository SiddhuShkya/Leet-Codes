SELECT name
FROM (
    SELECT name, COUNT(*)
    FROM (
        SELECT e1.name, e2.managerId
        FROM employee e1
        RIGHT JOIN employee e2
        ON e1.id = e2.managerId
        WHERE e1.id IS NOT NULL
    ) t
    GROUP BY name, managerId
    HAVING COUNT(*) >= 5
) t1;