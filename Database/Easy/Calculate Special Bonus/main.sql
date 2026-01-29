SELECT employee_id, bonus
FROM (
    SELECT
        employee_id,
        CASE
            WHEN employee_id % 2 = 1
                AND NOT REGEXP_LIKE(name, '^m', 'i')
            THEN salary
            ELSE 0
        END AS bonus
    FROM Employees
) t
ORDER BY employee_id;