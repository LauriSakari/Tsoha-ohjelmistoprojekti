from sqlalchemy.sql import text
from db import db

def send(user_id, date_of_time, start_time, end_time):
    print("jotain")
    print(user_id,date_of_time,start_time,end_time)
    sql = "INSERT INTO free_times (user_id, date_of_time, start_time, end_time) VALUES (:user_id, :date_of_time, :start_time, :end_time)"
    db.session.execute(text(sql), {"user_id":user_id, "date_of_time":date_of_time, "start_time":start_time, "end_time":end_time})
    db.session.commit()
    return True