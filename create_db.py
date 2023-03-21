import bcrypt
from flask import Flask
from ForumApp.extensions import db
from ForumApp.models.profile import Profile
from ForumApp.models.post import Post
from ForumApp.models.user import User
from ForumApp.models.role import Role
from ForumApp.models.comment import Comment
from ForumApp.models.board import Board
from config import Config
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()
    role1 = Role(role="ADMIN")
    role2 = Role(role="USER")
    db.session.add(role1)
    db.session.add(role2)
    db.session.commit()
    user1 = User()
    user1.role=Role.query.filter_by(id=1).first()
    user1.username='admin'
    bcrypt = Bcrypt(app)
    user1.password = bcrypt.generate_password_hash('admin')
    user2 = User()
    user2.role=Role.query.filter_by(id=2).first()
    user2.username='testuser'
    user2.password=bcrypt.generate_password_hash('testuser')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
