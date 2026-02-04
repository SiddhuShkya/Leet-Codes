SELECT 
    ROUND(
        COUNT(DISTINCT a.player_id) * 1.0 
        / COUNT(DISTINCT f.player_id),
        2
    ) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) f
LEFT JOIN Activity a
    ON a.player_id = f.player_id
    AND DATEDIFF(a.event_date, f.first_login) = 1;