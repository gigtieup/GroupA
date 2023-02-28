#!/usr/bin/env python3

import sqlite3
import cgi
import cgitb

# Enable detailed error messages in the browser
cgitb.enable()

# Parse the form data
form = cgi.FieldStorage()

# Get the value of the "data" field
data = form.getvalue('data')

# Connect to the database
conn = sqlite3.connect('example.db')

# Insert the data into the database
conn.execute('INSERT INTO data (input) VALUES (?)', [data])
conn.commit()

# Close the database connection
conn.close()

# Redirect the user back to the HTML page
print("Content-type: text/html")
print("Location: index.html")
print()