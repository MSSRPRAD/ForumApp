from ForumApp.auth import bp
from flask import render_template, flash

from flask_admin import Admin
from flask import render_template, redirect, url_for, session, request, Flask
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt

from ForumApp.models.user import User
from ForumApp.models.role import Role
from ForumApp.models.profile import Profile
from config import Config

from flask import current_app as app

bcrypt = Bcrypt(app)

from ForumApp.extensions import db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user:
        session.clear()
        flash("If you try to open this page after logging in you will be logged out automatically!")
        logout_user()
        redirect(url_for('auth.login'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash("")
                return redirect('/profile')
            else:
                flash("Wrong Password. Please Try Again!")
        else:
            flash("Invalid Credentials. Please Try Again!")
    return render_template('auth/login.html')

@login_required
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(username=username, password = hashed_password)
        role = Role.query.filter_by(role="ADMIN").first()
        new_user.role = role
        profile = Profile(about = "This is my profile!")
        new_user.profile = profile
        existing_user = User.query.filter_by(username=username).first()
        if (existing_user):
            # print('\nAlready Exists Error!\n', file=sys.stderr)
            flash("That name is already taken, please choose another")
            return render_template('auth/register.html')
        else:
            db.session.add(new_user)
            db.session.commit()
            flash("")
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')
