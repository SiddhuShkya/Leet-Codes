SELECT customer_id 
FROM (
    SELECT
        customer_id,
        COUNT(DISTINCT product_key) AS num_products_bought,
        (SELECT COUNT(*) FROM Product) AS total_products
    FROM Customer
    GROUP BY customer_id
)t
WHERE num_products_bought = total_products;