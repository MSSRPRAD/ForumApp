from flask import Flask
from ForumApp.extensions import db
import datetime
import string
from ForumApp.models.post import Post

app = Flask(__name__)

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    about = db.Column(db.String(1000), nullable = False)
    posts = db.relationship('Post', backref = 'board')
    date_created = db.Column(db.DateTime, default = datetime.datetime.utcnow())
