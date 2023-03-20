from flask import Flask
from ForumApp.extensions import db
import datetime
app = Flask(__name__)

from ForumApp.models.comment import Comment

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable = False)
    content = db.Column(db.String(10000), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref = 'post')
    date_created = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
