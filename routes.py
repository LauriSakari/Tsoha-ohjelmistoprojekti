from app import app
from flask import render_template, redirect, request, session
from os import getenv
import user_handling
from werkzeug.security import check_password_hash, generate_password_hash
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    user = user_handling.find_username(username)

    if not user:
        print("invalid username")
        return render_template("error.html", message="Invalid username")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session ["username"] = username
        else:
            return render_template("error.html", message="Invalid password")

    return redirect("/home")

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
        user_id = user_handling.add_user(username, hash_value)
    except Exception as e:
        return render_template("error.html", message = e)

    try:
        user_handling.add_userinfo(user_id, grade, style)
    except Exception as e:
        return render_template("error.html", message = e)
    
    session ["username"] = username
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")