from ForumApp.prof import bp
from flask import render_template
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask import current_app as app
bcrypt = Bcrypt(app)
from ForumApp.models.user import User
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
    return render_template('profile/profile.html', user = current_user, role_name = role_name)
