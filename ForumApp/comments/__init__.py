from flask import Blueprint

bp = Blueprint('comments', __name__)

from ForumApp.comments import routes
