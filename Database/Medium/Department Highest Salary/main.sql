SELECT Department.name AS Department, Employee.name as Employee, salary FROM Employee
JOIN Department ON Employee.departmentId = Department.Id
WHERE (departmentId, salary) IN
(SELECT departmentId, MAX(salary) 
FROM Employee
GROUP BY departmentId);
