import dbus.server

from ForumApp.models.role import Role
from ForumApp.prof import bp
from flask import render_template, redirect
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask import current_app as app
bcrypt = Bcrypt(app)
from ForumApp.models.user import User
from ForumApp.models.profile import Profile
from ForumApp.models.notification import Notification
from ForumApp.models.user import FriendRequest
from ForumApp import db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/profile')
@login_required
def index():
    role_name = "temp"
    if current_user.role_id == 1:
        role_name = "ADMIN"
    elif current_user.role_id == 2:
        role_name = "USER"
    profile = Profile.query.filter_by(user_id =current_user.id).first()
    return render_template('src/profile/profile.html', user = current_user, role_name = role_name, profile=profile, cond=False)

@bp.route('/users/<int:id>')
@login_required
def list_users(id):
    user = User.query.filter_by(id=id).first()
    role_name = user.role.role
    profile = user.profile
    return render_template('src/profile/profile.html', user = user, role_name = role_name, profile=profile, cond=True)


@bp.route('/profile/notifications')
@login_required
def notif():
    notifications = Notification.query.filter_by(user_id = current_user.id).order_by(Notification.date_created.desc()).all()
    return render_template('src/profile/notification.html', user=current_user, notifications = notifications)

@bp.route('/users')
@login_required
def view_user():
    users = User.query.all()
    return render_template('src/profile/users.html', users = users)

@bp.route('/users/request/<int:id>/')
@login_required
def request(id):
    existing = FriendRequest.query.filter_by(requesting_user_id=current_user.id, receiving_user_id=id).first()
    if existing:
        url = '/users/'+str(id)
        return redirect(url)
    else:
        friendRequest = FriendRequest()
        friendRequest.requesting_user_id = current_user.id
        friendRequest.receiving_user_id = id
        friendRequest.status = 0
        db.session.add(friendRequest)
        db.session.commit()
        notif = Notification()
        notif.user_id = id
        notif.message = current_user.username + ' has sent you a friend request!'
        db.session.add(notif)
        db.session.commit()
    return redirect('/users')

@bp.route('/profile/friends')
@login_required
def show_friends():
    friends = current_user.friends
    requests = FriendRequest.query.filter_by(receiving_user_id=current_user.id).all()
    return render_template('src/profile/friends.html', friends = friends, requests=requests, users = User.query.all(), current_user=current_user)


@bp.route('/users/request/<int:id>/accept')
@login_required
def accept_request(id):
    request = FriendRequest.query.filter_by(requesting_user_id=id, receiving_user_id = current_user.id).first()
    db.session.delete(request)
    db.session.commit()
    user = User.query.filter_by(id=id).first()
    user.friends.append(current_user)
    current_user.friends.append(user)
    db.session.commit()
    return redirect('/profile/friends')
