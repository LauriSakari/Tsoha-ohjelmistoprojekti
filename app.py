from flask import Flask
from flask import render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

from sqlalchemy.sql import text


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///lharjuko"
db = SQLAlchemy(app)

app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()

    if not user:
        print("invalid username")
        return redirect("/")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            print("salasana oikein")
            session ["username"] = username
        else:
            print("salasana väärin")

    return redirect("/")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    hash_value = generate_password_hash(password)
    print("hashvalue ", hash_value)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()

    session ["username"] = username
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")