## A basic Forum app using Flask microframeworkfor learning purposes.

## UPDATE: Added a 'Frontend' using TailwindCss.

# Note: This app uses the Flask Large Application structure.


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

#### NOTE: You need internet connection or the tailwindcss won't show up

#### NOTE: Just a minimum app. Many more features need to be added.

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

#### Note: You need to be LOGGED IN to be able to create boards/posts/comments. 

### Boards, Posts, Comments

Navigate to `/boards`

You can click on boards to view the posts in it and on posts to view the comments under it.

### Notification

If a board is created the admin gets a notification. If a post is created the creater of the board gets a notification. If a comment is created the creater of the post gets a notification.

### Profile

Navigate to /profile to see your profile. You can access your notifications box through this page.
