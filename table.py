import sqlite3

conn = sqlite3.connect('GroupA/stock.db')
c = conn.cursor()

c.execute("""CREATE TABLE stock (
    stock_name TEXT,
    total_shares INTEGER,
    multiplier INTEGER,
    outcome INTEGER
)""")


conn.commit()
conn.close()