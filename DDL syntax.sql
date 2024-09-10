SELECT l.library_name, COUNT(b.book_id) AS total_books
FROM Libraries l
JOIN Books b ON l.library_id = b.library_id
GROUP BY l.library_name;

SELECT u.username, b.title, l.loan_date, l.due_date
FROM Loans l
JOIN Users u ON l.user_id = u.user_id
JOIN Books b ON l.book_id = b.book_id
WHERE l.return_date IS NULL;

SELECT u.username, b.title, h.hold_date, CURRENT_DATE - h.hold_date AS days_waiting
FROM Holds h
JOIN Users u ON h.user_id = u.user_id
JOIN Books b ON h.book_id = b.book_id
WHERE h.hold_expiry_date > CURRENT_DATE;

SELECT c.category_name, COUNT(l.loan_id) AS total_loans
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Categories c ON b.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_loans DESC;

SELECT u.username, COUNT(l.loan_id) AS books_borrowed
FROM Loans l
JOIN Users u ON l.user_id = u.user_id
WHERE l.loan_date >= CURRENT_DATE - INTERVAL '1 month'
GROUP BY u.username
HAVING COUNT(l.loan_id) > 2;
