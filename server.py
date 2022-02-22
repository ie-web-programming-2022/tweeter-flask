from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash

tweeter = Flask(__name__)
tweeter.config["SECRET_KEY"] = "this is not secret, remember, change it!"
engine = create_engine("sqlite:///tweeter.db")

@tweeter.route("/")
def index():
    return render_template("index.html")

@tweeter.route("/register")
def register():
    pass

@tweeter.route("/register", methods=["POST"])
def handle_register():
    pass

@tweeter.route("/users")
def users():
    pass

@tweeter.route("/users/<user_id>")
def user_detail(user_id):
    pass

@tweeter.route("/login")
def login():
    return render_template("login.html")

@tweeter.route("/login", methods=["POST"])
def handle_login():
    pass

@tweeter.route("/logout")
def logout():
    pass

@tweeter.route("/tweet", methods=["POST"])
def handle_tweet():
    pass

@tweeter.route("/follow/<followee>")
def follow(followee):
    pass

tweeter.run(debug=True)