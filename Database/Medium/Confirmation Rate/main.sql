SELECT 
    s.user_id,
    ROUND(
        CASE 
            WHEN c.action_count IS NOT NULL THEN c.confirmed_count * 1.0 / c.action_count
            ELSE 0
        END, 2
    ) AS confirmation_rate
FROM signups s
LEFT JOIN (
    SELECT
        user_id,
        SUM(CASE WHEN action = 'timeout' THEN 1 ELSE 0 END) +
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS action_count,
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_count
    FROM confirmations
    GROUP BY user_id
) c
ON s.user_id = c.user_id;


