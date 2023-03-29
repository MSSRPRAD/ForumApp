from flask import Flask
from sqlalchemy.orm import backref

from ForumApp.extensions import db
import datetime

app = Flask(__name__)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
    children = db.relationship("Comment",
                            backref=backref('parent', remote_side=[id])
                            )
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

