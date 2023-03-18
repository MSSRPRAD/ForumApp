from flask import Flask
from ForumApp.extensions import db

from ForumApp.models.user import User

app = Flask(__name__)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=False)
    users = db.relationship('User', backref = 'role')
