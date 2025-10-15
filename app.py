from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
import config, users, sqlite3, spots, secrets, math

app = Flask(__name__)
app.secret_key = config.secret_key

@app.before_request
def check_session():
    public_paths = ["/", "/register", "/login"]
    if request.path.startswith("/static/"):
        return
    if not session.get("user_id") and request.path not in public_paths:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.route("/")
def login_page():
    user_id = session.get("user_id")
    session["csrf_token"] = secrets.token_hex(16)
    if user_id:
        return redirect("/home")
    else:
        return render_template("login.html")

@app.route("/home")
def index():
    if not session.get("user_id"):
        return redirect("/login")
    user_id = session.get("user_id")
    username = users.get_user(user_id)[1]

    spot_list = spots.get_latest_spots()
    messages = spots.get_latest_messages()

    return render_template("index.html", username=username, spot_list=spot_list, messages=messages)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", filled = {})

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        # Maximum lengths
        if len(username) > 20 or len(password1) > 20 or len(password2) > 20:
            abort(403)
        # Minimum lengths
        if len(username) < 3:
            flash("The username length has to be at least 3")
            filled = {"username": username}
            return render_template("register.html", filled=filled)
        
        if len(password1) < 4:
            flash("The password length has to be at least 4")
            filled = {"username": username}
            return render_template("register.html", filled=filled)

        if password1 != password2:
            flash("ERROR: Password mismatch")
            filled = {"username": username}
            return render_template("register.html", filled=filled)

        try:
            users.create_user(username, password1)
            flash("Registration succesful, please login")
            return redirect("/")
        except sqlite3.IntegrityError:
            flash ("ERROR: Username already in use")
            filled = {"username": username}
            return render_template("register.html", filled=filled)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(username) > 20 or len(password) > 20:
            abort(403)

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
        check_csrf()
        user_id = session["user_id"]
        content = request.form["content"]
        if len(content) > 1000:
            abort(403)
        spots.post_message(spot_id, user_id, content)
        return redirect(request.url)

@app.route("/add_spot", methods=["GET", "POST"])
def add_spot():
    if request.method == "GET":
        categories = spots.get_categories()
        aspects = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        filled = session.pop("refill_data", {})
        return render_template("add_spot.html" , categories=categories, aspects=aspects, filled=filled)

    if request.method == "POST":
        check_csrf()
        user_id = session["user_id"]
        country = request.form["country"]
        title = request.form["title"]
        max_incline = request.form["max_incline"]
        skill_level = request.form["skill_level"]
        aspect = request.form["aspect"]
        notes =  request.form["notes"]
        file = request.files["image"]

        session["refill_data"] = {
            "country": country,
            "title": title,
            "max_incline": max_incline,
            "skill_level": skill_level,
            "aspect": aspect,
            "notes": notes
            }
        
        filled = session["refill_data"]
        
        continent = str(spots.get_country_continent(country))
        if len(continent) > 100 or len(country) > 100 or len(title) > 100 or len(aspect) > 10 or len(skill_level) > 20 or len(max_incline) > 2:
            abort(403)

        if int(max_incline) > 90 or int(max_incline) < 0:
            flash("Slope incline must be between 0 and 90 degrees")
            categories = spots.get_categories()
            aspects = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
            return render_template("add_spot.html" , categories=categories, aspects=aspects, filled=filled)

        if "submit" in request.form:
            spot_id = spots.add_spot(user_id, continent, country, title, max_incline, skill_level, aspect, notes)

        session.pop("refill_data", None)           
        return redirect("/spot/" + str(spot_id))


@app.route("/browse")
@app.route("/browse/<int:page>")
def browse(page=1):
    page_size = 10

    continent = request.args.get("continent")
    country = request.args.get("country")
    skill_level = request.args.get("skill_level")

    spot_count = spots.spot_count(
        continent=continent,
        country=country,
        skill_level=skill_level
        )
    page_count = math.ceil(spot_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/browse/1")
    if page > page_count:
        return redirect("/browse/" + str(page_count))

    spot_list = spots.get_spots(page,
                                page_size,
                                continent=continent,
                                country=country,
                                skill_level=skill_level)
    

    categories = spots.get_categories()

    # Country filter based on continent

    if continent:
        filtered_countries = [c for c in categories["countries"] if c[3] == continent]
    
    else:
        filtered_countries = categories["countries"]

    categories["countries"] = filtered_countries

    # Retain selected filters in pagination

    selected_continent = continent
    selected_country = country
    selected_skill_level = skill_level

    return render_template(
        "/browse.html",
        page=page,
        page_count=page_count,
        spot_list=spot_list,
        categories=categories,
        selected_continent=selected_continent,
        selected_country=selected_country,
        selected_skill_level=selected_skill_level
        )

@app.route("/edit_spot/<int:spot_id>", methods=["GET", "POST"])
def edit_spot(spot_id):
    spot = spots.get_spot(spot_id)
    categories = spots.get_categories()
    aspects = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    if spot["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_spot.html", spot=spot, aspects=aspects, categories=categories)

    if request.method == "POST":
        check_csrf()
        country = request.form["country"]
        title = request.form["title"]
        max_incline = request.form["max_incline"]
        skill_level = request.form["skill_level"]
        aspect = request.form["aspect"]
        notes =  request.form["notes"]   
        continent = str(spots.get_country_continent(country))

        if len(continent) > 100 or len(country) > 100 or len(title) > 100 or len(aspect) > 10 or len(skill_level) > 20 or len(max_incline) > 3:
            abort(403)

        if "update" in request.form:
            spots.update_spot(continent, country, title, max_incline, skill_level, aspect, notes, spot_id)
        return redirect("/browse")
        
@app.route("/remove_spot/<int:spot_id>", methods=["GET", "POST"])
def remove_spot(spot_id):
    spot = spots.get_spot(spot_id)
    if spot["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove.html", spot=spot)
    if request.method == "POST":
        check_csrf()
        if "yes" in request.form:
            spots.remove_spot(spot["id"])
        return redirect("/browse")

@app.route("/remove_message/<int:message_id>", methods=["GET", "POST"])
def remove_message(message_id):
    message = spots.get_message(message_id)
    spot_id = message["spot_id"]
    if message["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_message.html", message=message)
    if request.method == "POST":
        check_csrf()
        if "yes" in request.form:
            spots.remove_message(message["id"])
        return redirect(f"/spot/{spot_id}")

@app.route("/edit_message/<int:message_id>", methods=["GET", "POST"])
def edit_message(message_id):
    message = spots.get_message(message_id)
    spot_id = message["spot_id"]
    if message["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_message.html", message=message)
    if request.method == "POST":
        check_csrf()
        if "update" in request.form:
            content = request.form["content"]
            spots.update_message(message["id"], content)
        return redirect(f"/spot/{spot_id}")


@app.route("/search")
def search():
    query = request.args.get("query")
    if query:
        if len(query) > 100:
            abort(403)
    results = spots.search(query) if query else []
    return render_template("search.html", query=query, results=results)

@app.route("/user/<int:user_id>", methods=["GET", "POST"])
def user(user_id):
    user_spot_list = spots.get_user_spots(user_id)
    user_message_list = spots.get_user_messages(user_id)
    user = users.get_user(user_id)

    if request.method == "GET":
        return render_template("user.html",
                                user=user,
                                user_message_list=user_message_list,
                                user_spot_list=user_spot_list)
    if request.method == "POST": # remove if not needed and fix route
        return None

@app.route("/browse_users")
@app.route("/browse_users/<int:page>")
def browse_users(page=1):
    page_size = 10
    users_count = users.users_count()
    page_count = math.ceil(users_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/browse_users/1")
    if page > page_count:
        return redirect("/browse_users/" + str(page_count))

    user_list = users.get_users(page, page_size)
    return render_template("browse_users.html", 
                           user_list=user_list, 
                           page=page, 
                           page_count=page_count)
