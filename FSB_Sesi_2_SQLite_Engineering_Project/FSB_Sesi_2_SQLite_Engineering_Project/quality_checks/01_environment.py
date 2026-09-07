from pathlib import Path
import sqlite3
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.warehouse import connect_db
p = ROOT / 'data/output/qc_env.db'
p.unlink(missing_ok=True)
try:
    c = connect_db(p)
    value = c.execute('PRAGMA foreign_keys').fetchone()[0]
    ok = value == 1
    print('PASS' if ok else 'FAIL', sqlite3.sqlite_version, value)
    c.close()
except Exception as exc:
    print('FAIL', type(exc).__name__, exc)
    ok = False
raise SystemExit(0 if ok else 1)
