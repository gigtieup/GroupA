import sqlite3

conn = sqlite3.connect("/GroupA/user.db")
c = conn.cursor()

command = """CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)"""

c.execute(command)