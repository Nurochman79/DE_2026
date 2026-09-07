from pathlib import Path
import json
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent
checks = []

def check(label, condition, detail=''):
    checks.append(bool(condition))
    status = 'PASS' if condition else 'FAIL'
    suffix = f' — {detail}' if detail else ''
    print(f'{status:4} {label}{suffix}')

check('Python 3.10+', sys.version_info >= (3, 10), sys.version.split()[0])
check('Root project', (ROOT / 'src' / 'warehouse.py').exists(), str(ROOT))
for name in ('users', 'products', 'transactions'):
    path = ROOT / 'data' / 'processed' / f'{name}.json'
    try:
        rows = json.loads(path.read_text(encoding='utf-8'))
        check(f'Input {name}', isinstance(rows, list) and len(rows) > 0, f'{len(rows)} rows')
    except Exception as exc:
        check(f'Input {name}', False, f'{type(exc).__name__}: {exc}')
try:
    import src.warehouse as warehouse
    check('Import src.warehouse', True, str(Path(warehouse.__file__).resolve()))
except Exception as exc:
    check('Import src.warehouse', False, f'{type(exc).__name__}: {exc}')
check('SQLite available', bool(sqlite3.sqlite_version), sqlite3.sqlite_version)
print()
print('READY FOR DEVELOPMENT' if all(checks) else 'FIX SETUP BEFORE DEVELOPMENT')
raise SystemExit(0 if all(checks) else 1)
