<h1>Powderatlas</h1>
<em>Social web application where users can create, share and view freeride spot recommendations.</em>

This is an assignment project for University of Helsinki's Databases and Web-Development course. Many of the features are still under development. As of now the application has the following features:

- User registration, login and logout.
- User session management and access rights.
- Users can create, view, edit and delete spots they have created.
- Users can view spots other users have created.
- Users can send comments on other users spots.
- Users can search spots in the application (as of now only rudimentary search from spot title and notes)

The complete application will have at least these features (along with better looking UI)
<ul>
<li>The user can create an account to the application and sign in to the application.</li>
<li>The user can add spot recommendations to the application. In addition, the user can edit and delete the recommendations they have added.</li>
<li>The user can view the spot recommendations added to the application. The users can view spot recommendations they have added and spot recommmendations made by other users.</li>
<li>The user can search spot recommendations using keywords or categories. The users can search both their own spot recommendations and spot recommendations made by other users.</li>
<li>The application has user pages that show statistics about each user and spot recommendations made by them.</li>
<li>The user can assign one or more categories for the spot recommendation. The available categories are stored in the database.</li>
<li>In addition to spot recommendations, the users can comment, review and rate the spot recommendations created by them or other users.</li>
</ul>
<br />

<h3>For local testing of the app</h3>

**Clone the repository to your local drive.**
Navigate to the directory where you want to add the repository directory.
> $ git clone git@github.com:tannitee/freeride_spot_review_webapp

Go to the newly created directory.
> $ cd freeride_spot_review_webapp

**Set up virtual environment for python3 and install flask**
In your application directory:

Install and activate virtual environment for python3.
> $ python3 -m venv venv

Then activate the virtual environment.
> $ source venv/bin/activate

After initializing virtual environment, install Flask for Python.
> $ (venv)../pip install flask

**Create database and populate with example data**
database.db is not included in the repository, so it must be built locally with the sql-schema found in the repository.
First, ensure that you have sqlite3 installed.
> $ (sudo) apt install sqlite3

To the application directory, create database.db using the provided schema.sql file.
> $ sqlite3 database.db < schema.sql

Populate database.db with dummy data (optional)
> $python3 populate_dummy.py

_Caution! If you want to use dummy data, it's mandatory to do this database population before logging in to the application. Do not create user in the application first, because this will mess up the database.db and you have to reinitialize it._

**Run the app on local web server**

To start local web server navigate to the application directory.
> $ flask run

Open your favorite web-browser and browse to:
> http://127.0.0.1:5000/

