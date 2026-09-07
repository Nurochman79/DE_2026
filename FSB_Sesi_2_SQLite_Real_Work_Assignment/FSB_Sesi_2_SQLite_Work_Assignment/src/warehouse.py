"""SOURCE OF TRUTH. Notebook hanya mengimpor function dari file ini."""
import sqlite3

def connect_db(path="data/output/app.db"):
    raise NotImplementedError("TODO connect_db + PRAGMA")
def create_schema(conn,schema_path="schema.sql"):
    raise NotImplementedError("TODO create_schema")
def load_master(conn,users,products):
    raise NotImplementedError("TODO load_master")
def load_transactions(conn,transactions):
    raise NotImplementedError("TODO load_transactions")
def query_counts(conn):
    raise NotImplementedError("TODO query_counts")
def query_revenue(conn):
    raise NotImplementedError("TODO query_revenue")
def query_top_products(conn,limit=3):
    raise NotImplementedError("TODO query_top_products")
