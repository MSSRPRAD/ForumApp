from flask import Flask, session
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from ForumApp.extensions import db
from flask_babel import Babel
from ForumApp.models.user import User
from ForumApp.models.profile import Profile
from ForumApp.models.comment import Comment
from ForumApp.models.post import Post
from ForumApp.models.role import Role
from ForumApp.models.board import Board
from ForumApp.models.notification import Notification

from ForumApp.extensions import db

from flask_ckeditor import CKEditor

ckeditor = CKEditor()


class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.role_id == 1:
            return True
        else:
            return False

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    ckeditor.init_app(app)
    babel = Babel(app)
    admin = Admin(app)
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Role, db.session))
    admin.add_view(MyModelView(Profile, db.session))
    admin.add_view(MyModelView(Post, db.session))
    admin.add_view(MyModelView(Comment, db.session))
    admin.add_view(MyModelView(Board, db.session))
    admin.add_view(MyModelView(Notification,db.session))

    login_manager = LoginManager(app)


    #Initialize Flask Extensions here
    db.init_app(app)

    #Register Blueprints here

    # Home page blueprint
    with app.app_context():
        # Main Blueprint
        from ForumApp.main import bp as main_bp
        app.register_blueprint(main_bp)

        # Authentication Blueprint
        from ForumApp.auth import bp as auth_bp
        app.register_blueprint(auth_bp)

        # Profile Blueprint
        from ForumApp.prof import bp as profile_bp
        app.register_blueprint(profile_bp)

        # Board Bluepring
        from ForumApp.boards import bp as board_bp
        app.register_blueprint(board_bp)

        # Post Blueprint
        from ForumApp.posts import bp as post_bp
        app.register_blueprint(post_bp)

        # Comments Blueprint
        from ForumApp.comments import bp as comment_bp
        app.register_blueprint(comment_bp)

    return app
