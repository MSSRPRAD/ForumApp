from flask import Flask
from ForumApp.extensions import db
import datetime

app = Flask(__name__)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    about = db.Column(db.String(300), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

