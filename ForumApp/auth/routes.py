# from flask import Flask, render_template, redirect, url_for, flash, session, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import login_user, LoginManager, current_user, logout_user
# from flask_bcrypt import Bcrypt
# from ForumApp.models.user import User
#
#
# app = Flask(__name__)
#
# bcrypt = Bcrypt(app)
#
# db = SQLAlchemy(app)
#
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     if current_user:
#         session.clear()
#         flash("If you try to open this page after logging in you will be logged out automatically!")
#         logout_user()
#         redirect(url_for('login'))
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user:
#             if bcrypt.check_password_hash(user.password, password):
#                 login_user(user)
#                 flash("")
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash("Wrong Password. Please Try Again!")
#         else:
#             flash("Invalid Credentials. Please Try Again!")
#     return render_template('auth/login.html')
#
# @app.route('/logout', methods = ['GET', 'POST'])
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
#
# @app.route('/register', methods = ['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = bcrypt.generate_password_hash(password)
#         new_user = User(username=username, password = hashed_password)
#         existing_user = User.query.filter_by(username=username).first()
#         if (existing_user):
#             # print('\nAlready Exists Error!\n', file=sys.stderr)
#             flash("That name is already taken, please choose another")
#             return render_template('auth/register.html')
#         else:
#             db.session.add(new_user)
#             db.session.commit()
#             flash("")
#             return redirect(url_for('login'))
#     return render_template('auth/register.html')
