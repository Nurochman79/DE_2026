from pathlib import Path
from src.io_utils import read_json, write_json
from src.warehouse import connect_db, create_schema, load_master, load_transactions, query_counts, query_revenue, query_top_products

OUT = Path('data/output')
DB = OUT / 'app.db'

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    DB.unlink(missing_ok=True)
    try:
        conn = connect_db(DB)
        create_schema(conn)
        users = read_json('data/processed/users.json')
        products = read_json('data/processed/products.json')
        transactions = read_json('data/processed/transactions.json')
        load_master(conn, users, products)
        loaded, rejected = load_transactions(conn, transactions)
        results = {
            'counts': query_counts(conn),
            'revenue': query_revenue(conn),
            'top_products': query_top_products(conn),
        }
        write_json('data/output/rejected_transactions.json', rejected)
        write_json('data/output/query_results.json', results)
        write_json('data/output/metrics.json', {
            'loaded_transactions': loaded,
            'rejected_transactions': len(rejected),
            **results,
        })
        print(f"[OK] counts={results['counts']}")
        print(f"[OK] rejected={len(rejected)}")
        print(f"[OK] revenue={results['revenue']}")
        print(f"[OK] top_products={results['top_products']}")
        conn.close()
    except NotImplementedError as exc:
        print(f'[PENDING] {exc}')
        raise SystemExit(1)

if __name__ == '__main__':
    main()
