from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
import config, users, sqlite3, spots

app = Flask(__name__)
app.secret_key = config.secret_key

@app.before_request
def check_session():
    if not session.get("user_id") and request.path != "/" and request.path != "/register" and request.path != "/login":
        abort(403)

@app.route("/")
def login_page():
    user_id = session.get("user_id")
    if user_id:
        return redirect("/home")
    else:
        return render_template("login.html")

@app.route("/home")
def index():
    if not session.get("user_id"):
        return redirect("/login")
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

@app.route("/spot/<int:spot_id>", methods=["GET", "POST"])
def spot(spot_id):
    spot = spots.get_spot(spot_id)
    messages = spots.get_messages(spot_id)
    if not spot:
        abort(404)
    if request.method == "GET":
        return render_template("spot.html", spot=spot, messages=messages)

    if request.method == "POST":
        user_id = session["user_id"]
        content = request.form["content"]
        spots.post_message(spot_id, user_id, content)
        return redirect(request.url)

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
        if len(area) > 100 or len(country) > 100 or len(title) > 100 or len(aspect) > 10 or len(skill_level) > 20 or len(max_incline) > 3:
            abort(403)

        if "submit" in request.form:
            spots.add_spot(user_id, area, country, title, max_incline, skill_level, aspect, notes)
        return redirect("/browse")

@app.route("/browse")
def browse():
    spot_list = spots.get_spots()
    return render_template("/browse.html", spot_list=spot_list)

@app.route("/edit_spot/<int:spot_id>", methods=["GET", "POST"])
def edit_spot(spot_id):
    spot = spots.get_spot(spot_id)
    if spot["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_spot.html", spot=spot)

    if request.method == "POST":
        area = request.form["area"]
        country = request.form["country"]
        title = request.form["title"]
        max_incline = request.form["max_incline"]
        skill_level = request.form["skill_level"]
        aspect = request.form["aspect"]
        notes =  request.form["notes"]
        if len(area) > 100 or len(country) > 100 or len(title) > 100 or len(aspect) > 10 or len(skill_level) > 20 or len(max_incline) > 3:
            abort(403)

        if "update" in request.form:
            spots.update_spot(area, country, title, max_incline, skill_level, aspect, notes, spot_id)
        return redirect("/browse")
        

@app.route("/remove_spot/<int:spot_id>", methods=["GET", "POST"])
def remove_spot(spot_id):
    spot = spots.get_spot(spot_id)
    if spot["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove.html", spot=spot)
    
    if request.method == "POST":
        if "yes" in request.form:
            spots.remove_spot(spot["id"])
        return redirect("/browse")


@app.route("/search")
def search():
    query = request.args.get("query")
    results = spots.search(query) if query else []
    return render_template("search.html", query=query, results=results)
