from app import app
from flask import render_template, redirect, request, session
from os import getenv
from sqlalchemy.exc import IntegrityError
import secrets
import user_handling
import messages
import time_slots
import utils
from werkzeug.security import check_password_hash, generate_password_hash
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    
    return render_template("index.html")

@app.route("/messages", methods=["GET"])
def messages_page():
    message_list = messages.get_list()
    return render_template("messages.html", count=len(message_list), messages=message_list)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

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
                session["csrf_token"] = secrets.token_hex(16)

            else:
                return render_template("error.html", message="Invalid password")

        return redirect("/login")

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

    if len(username) < 5 or not username.isalnum():
        return render_template("error.html", message="käyttäjänimi on liian lyhyt tai sisältää erikoismerkkejä, minimipituus 5 merkkiä")

    if len(password) < 8:
        return render_template("error.html", message="salasana on liian lyhyt, minimipituus 8 merkkiä")

    if password != request.form["verify_password"]:
        return render_template("error.html", message="salasanat eivät täsmää, yritä uudestaan")

    hash_value = generate_password_hash(password)

    try:
        user_id = user_handling.add_user(username, hash_value, grade, style)
    except IntegrityError:
        return render_template("error.html", message = "Käyttäjänimi on jo käytössä tai olet syöttänyt epäkelpoa tietoa")

    session ["username"] = username
    session ["user_id"] = user_id
    session["csrf_token"] = secrets.token_hex(16)

    return redirect("/")

@app.route("/send_message", methods=["POST"])
def send():
    content = request.form["content"]
    user_id = session["user_id"]
    utils.check_csrf_token()
    if messages.send(content, user_id):
        return redirect("/messages")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
    
@app.route("/remove_message", methods=["POST"])
def remove_message():
    utils.check_csrf_token()
    messages.remove_message(request.form["remove"])
    return redirect("/messages")

@app.route("/add_slot", methods=["GET", "POST"])
def add_slot():
    if request.method == "POST":
        utils.check_csrf_token()
        date = request.form["date"]
        starting_time = request.form["starting_time"]
        finishing_time = request.form["finising_time"]
        location = request.form["location"]

        try:
            time_slots.send(session["user_id"], date, starting_time, finishing_time, location)
        except IntegrityError:
            return render_template("error.html", message = "Tarkista että olet syöttänyt tiedot oikein. Aloitusajan täytyy olla aikaisempi kuin lopetusajan")
        
        return redirect("/")
    if request.method == "GET":
        locations = time_slots.get_locations()
        return render_template("add_slot.html", locations=locations)
    
@app.route("/free_slots", methods=["GET"])
def free_slots():
    times = time_slots.get_free_times(session.get("user_id"))
    return render_template("time_slots.html", count_times=len(times), times=times)


@app.route("/reserved_slots", methods=["GET", "POST"])
def reserve_slot():
    if request.method == "POST":
        utils.check_csrf_token()
        user = request.form["user"]
        date = request.form["date"]
        start_time = request.form["start_time"]
        end_time = request.form["end_time"]
        slot_id = request.form["id"]
        location = request.form["location"]
        time_slots.book_time(session["user_id"], slot_id)

        booked_times = time_slots.get_booked_times(session["user_id"])

        return render_template("bookings.html", info=[user, date, start_time, end_time, location], booked_times=booked_times)
    
    if request.method == "GET":
        booked_times = time_slots.get_booked_times(session["user_id"])

        return render_template("bookings.html", info=None, booked_times=booked_times)
        

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    return redirect("/")