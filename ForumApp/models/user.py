import os

from flask_login import UserMixin
from flask import Flask
from ForumApp.extensions import db

from ForumApp.models.post import Post
from ForumApp.models.comment import Comment
from ForumApp.models.profile import Profile
from ForumApp.models.notification import Notification

app = Flask(__name__)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    profile = db.relationship('Profile', backref='user', uselist = False)
    notifications = db.relationship('Notification', backref='user')
    posts = db.relationship('Post', backref = 'user')
    comments = db.relationship('Comment', backref = 'user')
