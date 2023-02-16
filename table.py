import sqlite3

conn = sqlite3.connect('stock.db')
c = conn.cursor()

c.execute("""CREATE TABLE stock (
    stock_name TEXT,
    shares INTEGER,
    share_price INTEGER,
    total INTEGER
)""")

conn.commit()
conn.close()