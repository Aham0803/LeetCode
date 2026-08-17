# Write your MySQL query statement below
select
l.book_id,
l.title,
l.author,
l.genre,
l.publication_year,
count(b.book_id) as current_borrowers
from library_books as l
LEFT join borrowing_records as b
on l.book_id = b.book_id
 AND b.return_date IS NULL
group by l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    l.total_copies
having count(b.book_id) = l.total_copies
ORDER BY current_borrowers DESC, l.title ASC;