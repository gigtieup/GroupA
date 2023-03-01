from flask import Flask, render_template, request, redirect, session
import sqlite3

def register_user(username, password):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('INSERT INTO users(username, password) value (?, ?)', (username,password))
    conn.commit()
    conn.close()

def check_user(username, password):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('Select username, password FROM users WHERE username=? and password=?', (username, password))

    result = c.fetchone()
    if result:
        return True
    else:
        return False
    

app = Flask(__name__)

app.secret_key = "123456"

@app.route("/")
def index():
    return render_template('CreateAccount.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        register_user(username, password)
        return redirect('/')
    else:
        return render_template(register.html)
    
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
        if check_user(username, password):
            session['username']=username

        return redirect('/home/')
    else:
        return redirect('/')
    
@app.route('/home', methods=["POST","GET"])
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return "Wrong Credentials"
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')   

if __name__ == '__main__':
    app.run(debug=True)