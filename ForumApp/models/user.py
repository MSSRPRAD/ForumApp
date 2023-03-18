from flask_login import UserMixin
from flask import Flask
from ForumApp.extensions import db

app = Flask(__name__)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile = db.relationship('Profile', backref='user', uselist = False)
    posts =db.relationship('Post', backref = 'user')
    comments = db.relationship('Comment', backref = 'user')
