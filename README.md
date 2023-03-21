## A basic Forum app using Flask microframework for learning purposes.

## EDIT:
Added a 'Frontend' using TailwindCss.


## To Install:

`git clone https://github.com/MSSRPRAD/ForumApp.git`

`cd ForumApp`

`virtualenv venv`

`source venv/bin/activate` (On Bash Terminal)

`pip install -r requirements.txt`

`export SECRET_KEY=SECRET_KEY`

`export FLASK_ENV=development`

`export FLASK_APP=ForumApp`

## -- CREATE DB --

`python create_db.py`

This creates an admin user with credentials:

username: admin

password: admin

and a regular user with credentials:

username: testuser

password: testuser

To Run the Application on localhost:

`flask run`

# NOTE: You need internet connection or the tailwindcss won't show up

# NOTE: Just a minimum app. Many more features need to be added.

## ADMIN FUNCTIONALITY:

Implemented from flask_admin

Navigate to '/admin/' (Logged in as Admin)

## LOGIN FUNCTIONALITY:

Navigate to /login

## LOGOUT FUNCTIONALITY:

Navigate to /logout

## REGISTER FUNCTIONALITY:

Navigate to /register

## FORUM FUNCTIONALITY:

Navigate to /board

Navigate to /board
