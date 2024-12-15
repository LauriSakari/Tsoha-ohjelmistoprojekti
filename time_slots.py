from sqlalchemy.sql import text
from db import db

def send(user_id, date_of_time, start_time, end_time, location):
    sql = """INSERT INTO free_times
        (user_id, date_of_time, start_time, end_time, location_id)
        VALUES (:user_id, :date_of_time, :start_time, :end_time, :location)"""
    db.session.execute(text(sql), \
        {"user_id":user_id,
         "date_of_time":date_of_time, 
         "start_time":start_time, 
         "end_time":end_time,
         "location":location})
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

def get_free_times(user_id):    
    sql = """
        SELECT U.username, F.date_of_time, 
        TO_CHAR(F.start_time, 'HH24.MI') AS start_time,
        TO_CHAR(F.end_time, 'HH24.MI') AS end_time, 
        F.id, L.name
        FROM free_times F JOIN users U ON F.user_id = U.id 
        LEFT JOIN booked_times B 
        ON F.id = B.free_time_id
        LEFT JOIN locations L 
        ON F.location_id = L.id 
        WHERE U.id != :user_id 
        AND B.user_id IS NULL"""
    
    result = db.session.execute(text(sql), {"user_id":user_id})
    return result.fetchall()

def get_booked_times(user_id):
    sql = """
    SELECT U.username, F.date_of_time,
    TO_CHAR(F.start_time, 'HH24.MI') AS start_time,
    TO_CHAR(F.end_time, 'HH24.MI') AS end_time, 
    F.id, L.name
    FROM free_times F JOIN users U 
    ON F.user_id = U.id
    JOIN booked_times B 
    ON F.id = B.free_time_id
    LEFT JOIN locations L 
    ON F.location_id = L.id 
    WHERE B.user_id = :user_id;
    """
    result = db.session.execute(text(sql), {"user_id":user_id})
    return result.fetchall()

def get_locations():
    sql = """SELECT id, name FROM locations"""
    result = db.session.execute(text(sql))
    return result.fetchall()