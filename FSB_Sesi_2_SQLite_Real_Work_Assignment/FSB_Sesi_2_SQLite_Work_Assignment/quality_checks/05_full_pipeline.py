from pathlib import Path
import json
import sqlite3
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.io_utils import read_json
from src.warehouse import connect_db, create_schema, load_master, load_transactions, query_counts, query_revenue, query_top_products
p = ROOT / 'data/output/qc_full.db'
p.unlink(missing_ok=True)
c = connect_db(p)
create_schema(c)
load_master(c, read_json(ROOT / 'data/processed/users.json'), read_json(ROOT / 'data/processed/products.json'))
loaded, rejected = load_transactions(c, read_json(ROOT / 'data/processed/transactions.json'))
counts = query_counts(c)
revenue = query_revenue(c)
top = query_top_products(c)
ok = counts == {'users': 14, 'products': 10, 'transactions': 22} and loaded == 22 and len(rejected) == 3 and revenue == 8745000 and top[:3] == [('P006', 'Webcam', 19), ('P008', 'Notebook', 2), ('P007', 'Desk Lamp', 1)]
print('PASS' if ok else 'FAIL', counts, revenue, top[:3], len(rejected))
c.close()
raise SystemExit(0 if ok else 1)
