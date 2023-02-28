from flask import Flask, render_template, request, 
import sqlite3
import requests

app = Flask(__name__)

@app.route('/')
def buy():
    return render_template('game.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    stocks = []
    total = 0

    if request.method == 'POST':
        conn = 

        c = conn.cursor()
        guest_vnaam = request.form.get('Voornaam')
        guest_anaam = request.form.get('Achternaam')
        guest_cnaam = request.form.get('Bedrijfsnaam')
        guest_datum = request.form.get('Datum')

        conn = sqlite3.connect('GroupA/stock.db')
        c = conn.cursor()
        c.execute("INSERT INTO stock (stock_name, total_share, shares, total) VALUES (?, ?, ?, ?)", (stock_name, shares, share_price, total_stock))
        conn.commit()

    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    c.execute("SELECT * FROM stock WHERE total > 0")
    stock = c.fetchall()

    return render_template('rec.html')

if __name__ == '__main__':
    app.run(debug=True)

