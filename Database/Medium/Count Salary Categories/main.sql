WITH all_categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)
SELECT 
    c.category,
    COUNT(t.category) AS accounts_count
FROM all_categories c
LEFT JOIN (
    SELECT
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
    FROM accounts
) t
ON c.category = t.category
GROUP BY c.category;