from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.io_utils import read_json
from src.warehouse import connect_db, create_schema, load_master
p = ROOT / 'data/output/qc_master.db'
p.unlink(missing_ok=True)
c = connect_db(p)
create_schema(c)
load_master(c, read_json(ROOT / 'data/processed/users.json'), read_json(ROOT / 'data/processed/products.json'))
a = c.execute('SELECT COUNT(*) FROM users').fetchone()[0]
b = c.execute('SELECT COUNT(*) FROM products').fetchone()[0]
ok = (a, b) == (14, 10)
print('PASS' if ok else 'FAIL', a, b)
c.close()
raise SystemExit(0 if ok else 1)
