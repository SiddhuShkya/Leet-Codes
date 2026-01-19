SELECT player_id, MAX(event_date) AS first_login
FROM Activity 
GROUP BY player_id;