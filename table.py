import sqlite3

conn = sqlite3.connect('GroupA/stock.db')
c = conn.cursor()

# c.execute("""CREATE TABLE stock (
#     stock_name TEXT,
#     total_shares INTEGER,
#     multiplier INTEGER,
#     outcome INTEGER
# )""")


c.execute("""CREATE TABLE stock_fact (
    stock_name TEXT,
    stock_fact TEXT
)""")

conn.commit()
conn.close()


