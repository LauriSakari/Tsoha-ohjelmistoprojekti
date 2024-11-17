from sqlalchemy.sql import text
from db import db

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U " \
          "WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(text(sql))
    return result.fetchall()


def send(content, user_id):
    sql = "INSERT INTO messages (content, user_id, sent_at) VALUES (:content, :user_id, NOW())"
    db.session.execute(text(sql), {"content":content, "user_id":user_id})
    db.session.commit()
    return True
