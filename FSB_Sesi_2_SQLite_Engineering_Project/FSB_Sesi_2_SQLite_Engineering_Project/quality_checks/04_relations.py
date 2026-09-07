from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.io_utils import read_json
from src.warehouse import connect_db, create_schema, load_master, load_transactions
p = ROOT / 'data/output/qc_relations.db'
p.unlink(missing_ok=True)
c = connect_db(p)
create_schema(c)
load_master(c, read_json(ROOT / 'data/processed/users.json'), read_json(ROOT / 'data/processed/products.json'))
loaded, rejected = load_transactions(c, read_json(ROOT / 'data/processed/transactions.json'))
actual = c.execute('SELECT COUNT(*) FROM transactions').fetchone()[0]
ok = (loaded, actual, len(rejected)) == (22, 22, 3)
print('PASS' if ok else 'FAIL', loaded, actual, len(rejected))
c.close()
raise SystemExit(0 if ok else 1)
