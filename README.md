<h1>Powderatlas</h1>
<em>Social web application where users can create, share and view freeride spot recommendations.</em>

This is an assignment project for University of Helsinki's Databases and Web-Development course.  
The application has following features:

- User registration, login and logout.
- User session management and access rights.
- Users can create, view, edit and delete spots they have created.
- Users can view spots other users have created.
- Users can send comments on other users spots.
- Users can search spots in the application.
- Users can view other users userpages which show page activity of the user.

<h3>For local testing of the app</h3>

**Clone the repository to your local drive.**
Navigate to the directory where you want to add the repository directory.
> $ git clone git@github.com:tannitee/freeride_spot_review_webapp

Go to the newly created directory.
> $ cd freeride_spot_review_webapp
pip
**Set up virtual environment for python3 and install flask**
In your application directory:

Install and activate virtual environment for python3.
> $ python3 -m venv venv

Then activate the virtual environment.
> $ source venv/bin/activate

After initializing virtual environment, install Flask for Python.
> $ (venv)../pip install flask

**Create database and populate with example data**
database.db is not included in the repository, so it must be built and initialized locally with the schema.sql and init.sql files found in the repository.
First, ensure that you have sqlite3 installed.
> $ (sudo) apt install sqlite3

To the application directory, create database.db using the provided schema.sql file:
> $ sqlite3 database.db < schema.sql

Initialize databaase.db with application data using provided init.sql file:
> $ sqlite3 database.db < init.sql

**Run the app on local web server**

To start local web server navigate to the application directory.
> $ flask run

Open your favorite web-browser and browse to:
> http://127.0.0.1:5000/

