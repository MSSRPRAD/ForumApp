from flask import Flask
from ForumApp.extensions import db
from ForumApp.models.profile import Profile
from ForumApp.models.post import Post
from ForumApp.models.user import User
from ForumApp.models.role import Role
from ForumApp.models.comment import Comment
from ForumApp.models.board import Board
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()
