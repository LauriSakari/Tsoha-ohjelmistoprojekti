from db import db
from sqlalchemy.sql import text

def add_user(username, hash_value, grade, style):
    sql = "INSERT INTO users (username, password, grade, efficient) VALUES (:username, :password, :grade, :efficient) RETURNING id"
    result = db.session.execute(text(sql), {"username":username, "password":hash_value, "grade":grade, "efficient":style})
    db.session.commit()
    return result.fetchone()[0]

def find_username(username):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    return result.fetchone()
