import datetime
import os

from flask_login import UserMixin
from flask import Flask
from ForumApp.extensions import db


app = Flask(__name__)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
