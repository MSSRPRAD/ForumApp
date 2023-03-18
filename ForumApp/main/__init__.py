from flask import Blueprint

bp = Blueprint('main', __name__)

from ForumApp.main import routes

