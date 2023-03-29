import os
from datetime import datetime

from flask_login import UserMixin
from flask import Flask
from ForumApp.extensions import db

from ForumApp.models.post import Post
from ForumApp.models.comment import Comment
from ForumApp.models.profile import Profile
from ForumApp.models.notification import Notification
from ForumApp.models.board import Board
from sqlalchemy.ext.associationproxy import association_proxy

app = Flask(__name__)

friendship = db.Table(
    'friendships',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), index=True),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id')),
    db.UniqueConstraint('user_id', 'friend_id', name='unique_friendships'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    profile = db.relationship('Profile', backref='user', uselist=False)
    notifications = db.relationship('Notification', backref='user')
    posts = db.relationship('Post', backref='user')
    boards = db.relationship('Board', backref='user')
    comments = db.relationship('Comment', backref='user')
    requests = association_proxy('received_rels', 'requesting_user')
    requested = association_proxy('requested_rels', 'receiving_user')

    requested_rels = db.relationship(
        'FriendRequest',
        foreign_keys='FriendRequest.requesting_user_id',
        backref='requesting_user'
    )
    received_rels = db.relationship(
        'FriendRequest',
        foreign_keys='FriendRequest.receiving_user_id',
        backref='receiving_user'
    )

    friends = db.relationship('User',
                              secondary=friendship,
                              primaryjoin=id == friendship.c.user_id,
                              secondaryjoin=id == friendship.c.friend_id)

class FriendRequest(db.Model):
    requesting_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    receiving_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String(200), nullable=False)
