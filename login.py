import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()


# c.execute("""CREATE TABLE account (
#     username TEXT,
#     password TEXT
# )""")


conn.commit()
conn.close()
