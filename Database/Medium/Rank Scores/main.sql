SELECT s1.Score, (SELECT COUNT(DISTINCT Score) FROM Scores s2 WHERE s2.Score >= s1.Score) AS 'Rank'
FROM Scores s1
ORDER BY s1.Score Desc