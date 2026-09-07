from pathlib import Path
import json
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent
DB = ROOT / 'data/output/app.db'
failures = []

if not DB.exists():
    print('FAIL missing app.db')
    raise SystemExit(1)

conn = sqlite3.connect(DB)
conn.execute('PRAGMA foreign_keys=ON')
counts = {name: conn.execute(f'SELECT COUNT(*) FROM {name}').fetchone()[0] for name in ('users','products','transactions')}
expected_counts = {'users': 14, 'products': 10, 'transactions': 22}
print('PASS' if counts == expected_counts else 'FAIL', 'counts', counts)
if counts != expected_counts:
    failures.append('counts')

fk_on = conn.execute('PRAGMA foreign_keys').fetchone()[0] == 1
print('PASS' if fk_on else 'FAIL', 'foreign_keys')
if not fk_on:
    failures.append('foreign_keys')

fk_list = conn.execute('PRAGMA foreign_key_list(transactions)').fetchall()
print('PASS' if len(fk_list) == 2 else 'FAIL', 'transaction_fks', len(fk_list))
if len(fk_list) != 2:
    failures.append('transaction_fks')

revenue = conn.execute('SELECT SUM(t.quantity*p.price) FROM transactions t JOIN products p ON t.product_id=p.product_id').fetchone()[0]
print('PASS' if revenue == 8745000 else 'FAIL', 'revenue', revenue)
if revenue != 8745000:
    failures.append('revenue')

top = conn.execute('SELECT p.product_id,p.name,SUM(t.quantity) units FROM products p JOIN transactions t ON p.product_id=t.product_id GROUP BY p.product_id,p.name ORDER BY units DESC,p.product_id LIMIT 3').fetchall()
expected_top = [('P006', 'Webcam', 19), ('P008', 'Notebook', 2), ('P007', 'Desk Lamp', 1)]
print('PASS' if top == expected_top else 'FAIL', 'top_products', top)
if top != expected_top:
    failures.append('top_products')
conn.close()

reject_path = ROOT / 'data/output/rejected_transactions.json'
if reject_path.exists():
    rejected = json.loads(reject_path.read_text(encoding='utf-8'))
    ids = sorted([row.get('tx_id') for row in rejected])
    ok = len(rejected) == 3 and ids == ['T023', 'T024', 'T025'] and all(row.get('reason') for row in rejected)
    print('PASS' if ok else 'FAIL', 'rejected_log', ids)
    if not ok:
        failures.append('rejected_log')
else:
    print('FAIL rejected_log missing file')
    failures.append('rejected_log')

print()
print('READY FOR REVIEW' if not failures else f"NOT COMPLETE: {', '.join(failures)}")
raise SystemExit(0 if not failures else 1)
