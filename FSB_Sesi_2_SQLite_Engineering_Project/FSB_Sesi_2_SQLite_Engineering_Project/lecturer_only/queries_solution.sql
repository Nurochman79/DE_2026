SELECT COUNT(*) FROM users; SELECT COUNT(*) FROM products; SELECT COUNT(*) FROM transactions;
SELECT SUM(t.quantity*p.price) FROM transactions t JOIN products p ON t.product_id=p.product_id;
SELECT p.product_id,p.name,SUM(t.quantity) units FROM products p JOIN transactions t ON p.product_id=t.product_id GROUP BY p.product_id,p.name ORDER BY units DESC LIMIT 3;