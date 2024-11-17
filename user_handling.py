from db import db
from sqlalchemy.sql import text

def add_user(username, hash_value):
    sql = "INSERT INTO users (username, password) VALUES (:username, :password) RETURNING id"
    result = db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()
    return result.fetchone()[0]

def add_userinfo(user_id, grade, style):
    sql = "INSERT INTO user_info (user_id, grade, efficient) VALUES (:user_id, :grade, :efficient)"
    db.session.execute(text(sql), {"user_id":user_id, "grade":grade, "efficient":style})
    db.session.commit()

def find_username(username):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    return result.fetchone()
