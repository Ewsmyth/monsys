from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/")
def auth_login():
    return "Hello World"