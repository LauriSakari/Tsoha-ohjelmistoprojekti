from sqlalchemy.sql import text
from db import db

def send(user_id, date_of_time, start_time, end_time):
    sql = """INSERT INTO free_times
        (user_id, date_of_time, start_time, end_time)
        VALUES (:user_id, :date_of_time, :start_time, :end_time)"""
    db.session.execute(text(sql), \
        {"user_id":user_id,
         "date_of_time":date_of_time, 
         "start_time":start_time, 
         "end_time":end_time})
    db.session.commit()
    return True

def book_time(user_id, free_time_id):
    sql = """INSERT INTO booked_times
        (user_id, free_time_id)
        VALUES (:user_id, :free_time_id)"""
    db.session.execute(text(sql),\
        {"user_id":user_id,
         "free_time_id":free_time_id})
    db.session.commit()

def get_free_times():
    sql = """SELECT U.username, F.date_of_time,
        TO_CHAR(F.start_time, 'HH24.MI') AS start_time,
        TO_CHAR(F.end_time, 'HH24.MI') AS end_time, F.id
        FROM free_times F, users U WHERE F.user_id != U.id;"""
    result = db.session.execute(text(sql))
    return result.fetchall()

def get_booked_times(user_id):
        sql = """SELECT U.username, F.date_of_time,
        TO_CHAR(F.start_time, 'HH24.MI') AS start_time,
        TO_CHAR(F.end_time, 'HH24.MI') AS end_time, F.id
        FROM free_times F, users U, booked_times B 
        WHERE F.id = B.free_time_id AND B.user_id = U.id AND U.id = :user_id;"""
        result = db.session.execute(text(sql), {"user_id":user_id})
        return result.fetchall()