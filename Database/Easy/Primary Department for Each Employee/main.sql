SELECT employee_id, department_id
FROM employee
WHERE primary_flag = 'Y'
UNION ALL
SELECT e.employee_id, e.department_id
FROM employee e
WHERE e.primary_flag = 'N'
  AND (
        SELECT COUNT(*)
        FROM employee e2
        WHERE e2.employee_id = e.employee_id
      ) = 1;