# import "packages" from flask
from flask import Flask, render_template, request, redirect, session  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition
import sqlite3 #import sqlite library for database
app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

def register_user(username, password):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('INSERT INTO users(username, password) values (?, ?)', (username, password))
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

app.secret_key = "123456"

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("home.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/registeri/')
def registeri():
    return render_template("register.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user(username, password):
            return "user already exist"
        else:
            register_user(username, password)
            return redirect('/')
    
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
        if check_user(username, password):
            session['username']=username

        return redirect('/home')
    else:
        return redirect('/')
    
@app.route('/home', methods=["POST","GET"])
def home():
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    else:
        return "Wrong Credentials"
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')   

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
