from flask import Flask
from flask import flash, redirect, render_template, request, session
import config, db, users, sqlite3, spots

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/home")
def index():
    username = users.get_username(session["user_id"])
    return render_template("index.html", username=username)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            flash("ERROR: Password mismatch")
            return redirect("/register")

        try:
            users.create_user(username, password1)
            flash("Registration succesful, please login")
            return redirect("/")
        except sqlite3.IntegrityError:
            flash ("ERROR: Username already in use")
            return redirect("/register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            return redirect("/home")
        else:
            flash("ERROR: Wrong username or password")
            return redirect("/")


@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")


@app.route("/add_spot", methods=["GET", "POST"])
def add_spot():
    if request.method == "GET":
        return render_template("add_spot.html")

    if request.method == "POST":
        user_id = session["user_id"]
        area = request.form["area"]
        country = request.form["country"]
        title = request.form["title"]
        max_incline = request.form["max_incline"]
        skill_level = request.form["skill_level"]
        aspect = request.form["aspect"]
        notes =  request.form["notes"]
        sql = ("""INSERT INTO spots (user_id, area, country, title, max_incline, skill_level, aspect, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
               """)
        db.execute(sql, [user_id, area, country, title, max_incline, skill_level, aspect, notes])
        return redirect("/browse")

@app.route("/browse")
def browse():
    spot_list = spots.get_spots()
    return render_template("/browse.html", spot_list=spot_list)
