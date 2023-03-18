from flask import Blueprint

bp = Blueprint('auth', __name__)

from ForumApp.auth import routes
