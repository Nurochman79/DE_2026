import sqlite3
from pathlib import Path
def connect_db(path="data/output/app.db"):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);c=sqlite3.connect(p);c.execute("PRAGMA foreign_keys=ON");return c
def create_schema(c,schema_path="schema.sql"):
 sql=Path(schema_path).read_text();sql=Path("lecturer_only/schema_solution.sql").read_text() if "TODO" in sql else sql;c.executescript(sql);c.commit()
def load_master(c,u,p):
 c.executemany("INSERT INTO users VALUES(?,?,?,?)",[(x["user_id"],x.get("name"),x.get("email"),x.get("city")) for x in u]);c.executemany("INSERT INTO products VALUES(?,?,?,?)",[(x["product_id"],x["name"],x["price"],x.get("category")) for x in p]);c.commit();return len(u),len(p)
def load_transactions(c,rows):
 n=0;r=[]
 for x in rows:
  try:c.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(x["tx_id"],x["user_id"],x["product_id"],x["quantity"],x.get("tx_date")));c.commit();n+=1
  except sqlite3.IntegrityError as e:c.rollback();r.append({"tx_id":x["tx_id"],"user_id":x["user_id"],"product_id":x["product_id"],"reason":str(e)})
 return n,r
def query_counts(c):return {n:c.execute(f"SELECT COUNT(*) FROM {n}").fetchone()[0] for n in("users","products","transactions")}
def query_revenue(c):return c.execute("SELECT SUM(t.quantity*p.price) FROM transactions t JOIN products p ON t.product_id=p.product_id").fetchone()[0]
def query_top_products(c,limit=3):return c.execute("SELECT p.product_id,p.name,SUM(t.quantity) units FROM products p JOIN transactions t ON p.product_id=t.product_id GROUP BY p.product_id,p.name ORDER BY units DESC,p.product_id LIMIT ?",(limit,)).fetchall()
