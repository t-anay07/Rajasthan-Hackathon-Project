import os

import mysql.connector as connection
conn = connection.connect(host = 'localhost', user = "root", password = "VM@152225@SM", use_pure = True, database = "login_info")
cur = conn.cursor()
# cur.execute("show databases")


import flask
from flask import Flask, render_template, redirect,jsonify, request, session

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/owner')
def owner():
    return render_template('owner.html')

@app.route('/farmer')
def farmer():
    return render_template('farmer.html')

@app.route('/submit', methods = ["POST"])
def form():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    password = str(request.form.get('password'))
    cur.execute("use login_info")
    query = " INSERT INTO credentials values(%s, %s, %s, %s)"
    val = [(name, mobile, email, password )]
    cur.executemany(query, val)
    conn.commit()
    return render_template("signin.html")


@app.route('/submit1', methods = ["POST"])
def form1():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    password = str(request.form.get('password'))
    cur.execute("use login_info")
    query = " INSERT INTO credentials1 values(%s, %s, %s, %s)"
    val = [(name, mobile, email, password )]
    cur.executemany(query, val)
    conn.commit()
    return render_template("signin2.html")


@app.route('/owner' , methods = ["POST"])
def sign_in():
    email = request.form.get('email')
    password = str(request.form.get('password'))
    cur.execute("""SELECT * FROM `credentials` WHERE `email` LIKE 'email' AND `password` LIKE 'password' """.format(email,password))
    cred=cur.fetchall()
    return redirect("owner")

@app.route('/farmer' , methods = ["POST"])
def sign_in1():
    email = request.form.get('email')
    password = str(request.form.get('password'))
    cur.execute("""SELECT * FROM `credentials1` WHERE `email` LIKE 'email' AND `password` LIKE 'password' """.format(email,password))
    cred=cur.fetchall()
    return redirect("farmer")



@app.route('/signin')
def member():
    return render_template('signin.html')

@app.route('/signin2')
def member2():
    return render_template('signin2.html')

@app.route('/register')
def resitration():
    return render_template('register.html')

@app.route('/register2')
def resitration2():
    return render_template('register2.html')



if __name__ == ('__main__'):
    app.run(debug=True)




