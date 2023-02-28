import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Set up the SQLite database
conn = sqlite3.connect('/GroupA/stock.db')
c = conn.cursor()

# Create the stocks table
c.execute('''CREATE TABLE Stocks
             (name text, price real, multiplier real)''')

# Insert sample data
c.execute("INSERT INTO stocks VALUES ('Stock 1', 10.0, 1.5)")
c.execute("INSERT INTO stocks VALUES ('Stock 2', 20.0, 2.0)")
c.execute("INSERT INTO stocks VALUES ('Stock 3', 30.0, 1.8)")
c.execute("INSERT INTO stocks VALUES ('Stock 4', 40.0, 1.2)")
c.execute("INSERT INTO stocks VALUES ('Stock 5', 50.0, 1.0)")

# Create the first HTML page
@app.route('/')
def index():
    return render_template('/templates/game.html')

# Handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the form data
    data = request.form.to_dict()
    
    # Store the data in the database
    for name, shares in data.items():
        shares = int(shares)
        c.execute("UPDATE stocks SET shares=? WHERE name=?", (shares, name))
    conn.commit()
    
    # Redirect the user to the second page
    return redirect('/result')

# Create the second HTML page
@app.route('/result')
def result():
    # Retrieve the data from the database
    c.execute("SELECT * FROM stocks")
    data = c.fetchall()
    
    # Calculate the final outcome
    rows = []
    for name, price, multiplier, shares in data:
        outcome = price * multiplier * shares
        rows.append((name, shares, multiplier, outcome))
    
    # Render the table
    return render_template('/templates/gamee.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)