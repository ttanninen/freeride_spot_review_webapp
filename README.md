<h1>Powderatlas</h1>
Social web application where users can create, share and view freeride spot recommendations.

This is an assignment project for University of Helsinki's Databases and Web-Development course.

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
$ git clone git@github.com:tannitee/freeride_spot_review_webapp

**Create database**
database.db is not included in the repository, so it must be built locally with the sql-schema found in the repository.
First, ensure that you have sqlite3 installed.
$ (sudo) apt install sqlite3

Create database.db using the schema.sql file.
$ sqlite3 database.db < schema.sql

**Set up virtual environment for python3 and install flask**

Install and activate virtual environment for python3.
$ python3 -m venv venv
$ source venv/bin/activate

After initializing virtual environment, install Flask for Python.
$ (venv)../pip install flask

**Run the app on local web server**

To start local web server navigate to the application directory.
$ flask run

Open your favorite web-browser and browse to:
http://127.0.0.1:5000/

