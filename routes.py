from app import app
from flask import render_template, redirect, request, session
from os import getenv
from sqlalchemy.exc import IntegrityError
import user_handling
import messages
import time_slots
from werkzeug.security import check_password_hash, generate_password_hash
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    user = user_handling.find_username(username)

    if not user:
        return render_template("error.html", message="Invalid username")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session ["username"] = username
            session ["user_id"] = user.id
        else:
            return render_template("error.html", message="Invalid password")

    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    if len(request.form) < 5:
        return render_template("error.html", message="Täytä kaikki kentät")

    username = request.form["username"]
    password = request.form["password"]
    grade = request.form["grade"]
    style = request.form["style"]

    if password != request.form["verify_password"]:
        return render_template("error.html", message="salasanat eivät täsmää, yritä uudestaan")

    hash_value = generate_password_hash(password)

    try:
        user_id = user_handling.add_user(username, hash_value)
    except IntegrityError:
        return render_template("error.html", message = "Käyttäjänimi on jo käytössä")
    try:
        user_handling.add_userinfo(user_id, grade, style)
    except Exception as e:
        return render_template("error.html", message = e)

    session ["username"] = username
    session ["user_id"] = user_id

    return redirect("/")

@app.route("/send_message", methods=["POST"])
def send():
    content = request.form["content"]
    user_id = session["user_id"]
    if messages.send(content, user_id):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/add_slot", methods=["GET", "POST"])
def add_slot():
    if request.method == "POST":
        print(request.form)
        date = request.form["date"]
        starting_time = request.form["starting_time"]
        finishing_time = request.form["finising_time"]

        print(session["user_id"], date, starting_time, finishing_time)

        
        result = time_slots.send(session["user_id"], date, starting_time, finishing_time)

        print(result)
        return redirect("/")
    if request.method == "GET":
        return render_template("add_slot.html")

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    return redirect("/")