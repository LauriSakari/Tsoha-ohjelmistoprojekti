from sqlalchemy.sql import text
from db import db

def send(user_id, date_of_time, start_time, end_time):
    sql = "INSERT INTO free_times \
        (user_id, date_of_time, start_time, end_time) \
        VALUES (:user_id, :date_of_time, :start_time, :end_time)"
    db.session.execute(text(sql), \
        {"user_id":user_id, 
         "date_of_time":date_of_time, 
         "start_time":start_time, 
         "end_time":end_time})
    db.session.commit()
    return True

def get_free_times():
    sql = "SELECT U.username, F.date_of_time, TO_CHAR(F.start_time, 'HH24.MI'), TO_CHAR(F.end_time, 'HH24.MI') FROM free_times F, users U WHERE F.user_id = U.id;"
    result = db.session.execute(text(sql))
    return result.fetchall()