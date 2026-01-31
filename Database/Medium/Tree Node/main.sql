SELECT 
    t1.id,
    CASE
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t1.id IN (
            SELECT p_id 
            FROM tree 
            WHERE p_id IS NOT NULL
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM tree t1;