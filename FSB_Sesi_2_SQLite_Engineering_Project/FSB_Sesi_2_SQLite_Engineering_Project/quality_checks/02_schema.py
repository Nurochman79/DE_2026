from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.warehouse import connect_db, create_schema
p = ROOT / 'data/output/qc_schema.db'
p.unlink(missing_ok=True)
try:
    c = connect_db(p)
    create_schema(c)
    tables = {row[0] for row in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    fks = c.execute('PRAGMA foreign_key_list(transactions)').fetchall()
    ok = {'users', 'products', 'transactions'} <= tables and len(fks) == 2
    print('PASS' if ok else 'FAIL', tables, len(fks))
    c.close()
except Exception as exc:
    print('FAIL', type(exc).__name__, exc)
    ok = False
raise SystemExit(0 if ok else 1)
