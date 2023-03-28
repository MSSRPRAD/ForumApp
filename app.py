# import the create app application factory
from ForumApp import create_app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user

from ForumApp.models.user import User
from ForumApp.models.profile import Profile
from ForumApp.models.comment import Comment
from ForumApp.models.post import Post
from ForumApp.models.role import Role
from ForumApp.models.board import Board
from ForumApp.models.notification import Notification
from ForumApp.extensions import db

app = create_app()


class MyModelView(ModelView):
   def is_accessible(self):
      if current_user.is_authenticated and current_user.role_id == 1:
         return True
      else:
         return False

if __name__ == '__main__':

   login_manager = LoginManager(app)

   admin = Admin(app)
   admin.add_view(MyModelView(User, db.session))
   admin.add_view(MyModelView(Role, db.session))
   admin.add_view(MyModelView(Profile, db.session))
   admin.add_view(MyModelView(Post, db.session))
   admin.add_view(MyModelView(Comment, db.session))
   admin.add_view(MyModelView(Board), db.session)
   admin.add_view(MyModelView(Notification), db.session)

   app.run()


