WITH user_stats AS (
    SELECT 
        user_id,
        COUNT(*) AS prompt_count,
        ROUND(AVG(tokens), 2) AS avg_tokens
    FROM prompts
    GROUP BY user_id
    HAVING COUNT(*) >= 3
)
SELECT 
    s.user_id,
    s.prompt_count,
    s.avg_tokens
FROM user_stats s
WHERE EXISTS (
    SELECT 1
    FROM prompts p
    WHERE p.user_id = s.user_id
      AND p.tokens > s.avg_tokens
)
ORDER BY s.avg_tokens DESC, s.user_id ASC;