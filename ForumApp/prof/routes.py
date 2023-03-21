from ForumApp.prof import bp
from flask import render_template
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask import current_app as app
bcrypt = Bcrypt(app)
from ForumApp.models.user import User
from ForumApp.models.profile import Profile
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
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    return render_template('src/profile/profile.html', user = current_user, role_name = role_name, profile=profile)
