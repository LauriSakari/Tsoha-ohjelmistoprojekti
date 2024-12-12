from flask import abort, request, session


def check_csrf_token():
    if session["csrf_token"] != request.form.get("csrf_token"):
        abort(403)