SELECT actor_id, director_id FROM (
    SELECT actor_id, director_id, COUNT(*) AS cnt
    FROM actordirector
    GROUP BY actor_id, director_id
    HAVING COUNT(*) >= 3
)t;

