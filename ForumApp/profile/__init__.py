from flask import Blueprint

bp = Blueprint('profile', __name__)

from ForumApp.profile import routes
