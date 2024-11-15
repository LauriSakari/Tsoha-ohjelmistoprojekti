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
        return render_template("error.html", message="Invalid username")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            print("salasana oikein")
            session ["username"] = username
        else:
            print("salasana väärin")
            return render_template("error.html", message="Invalid password")

    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    print("request form", request.form)
    username = request.form["username"]
    password = request.form["password"]
    grade = request.form["grade"]
    style = request.form["style"]
    # description = request.form["description"]

    if password != request.form["verify_password"]:
        return render_template("error.html", message="salasanat eivät täsmää, yritä uudestaan")

    hash_value = generate_password_hash(password)

    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(text(sql), {"username":username, "password":hash_value})
        db.session.commit()
    except Exception as e:
        return render_template("error.html", message = e)
    

    sql = "SELECT id FROM users WHERE username = :username"
    result = db.session.execute(text(sql), {"username":username})
    user_id  = result.fetchone()[0]

    try:
        sql = "INSERT INTO user_info (user_id, grade, efficient) VALUES (:user_id, :grade, :efficient)"
        db.session.execute(text(sql), {"user_id":user_id, "grade":grade, "efficient":style})
        db.session.commit()
    except Exception as e:
        return render_template("error.html", message = e)
    
    session ["username"] = username
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")