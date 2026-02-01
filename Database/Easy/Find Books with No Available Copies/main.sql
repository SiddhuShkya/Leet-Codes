SELECT 
    t1.book_id,
    t1.title,
    t1.author,
    t1.genre,
    t1.publication_year,
    t2.current_borrowers
FROM library_books t1
JOIN (
    SELECT 
        book_id,
        SUM(CASE WHEN return_date IS NULL THEN 1 ELSE 0 END) AS current_borrowers
    FROM borrowing_records
    GROUP BY book_id
) t2
ON t1.book_id = t2.book_id
WHERE t1.total_copies - t2.current_borrowers = 0
ORDER BY t2.current_borrowers DESC, t1.title ASC;