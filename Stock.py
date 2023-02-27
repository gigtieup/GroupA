from flask import Flask, render_template, request
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

    for stock_name in request.form.getlist('stock_name'):
        shares = int(request.form[stock_name])
        response = request.get("https://api.twelvedata.com/quote?symbol=${tickerSymbol}&apikey=${api}".format(stock_name))
        share_price = int(share_price)
        total_stock = share_price * shares
        total += total_stock
        stocks.append({
            'name': stock_name,
            'shares': shares,
            'share_price': share_price,
            'total_share': shares * share_price,
            'total': total_stock
            })

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

