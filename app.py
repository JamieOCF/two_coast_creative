from flask import Flask, render_template
from flask import session, redirect, url_for, g, request
from database import get_db, close_db 
from flask_session import Session
# from werkzeug.security import generate_password_hash, check_password_hash
# from forms import
# from functools import wraps


app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.teardown_appcontext(close_db)


@app.route("/", methods=["GET", "POST"])
def _():
    db = get_db()
    # __ = db.execute(""";""").fetch()
    # form = Form()
    # if form.validate_on_submit():
    #     return
    return render_template("base.html", )