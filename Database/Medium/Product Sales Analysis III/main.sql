SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM sales s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM sales
    GROUP BY product_id
) first_years
ON s.product_id = first_years.product_id
   AND s.year = first_years.first_year;