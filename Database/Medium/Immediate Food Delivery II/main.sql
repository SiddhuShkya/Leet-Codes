SELECT 
    ROUND(
        SUM(
            CASE 
                WHEN d.order_date = d.customer_pref_delivery_date THEN 1 
                ELSE 0 
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS immediate_percentage
FROM delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS first_date
    FROM delivery
    GROUP BY customer_id
) t
ON d.customer_id = t.customer_id
AND d.order_date = t.first_date;
