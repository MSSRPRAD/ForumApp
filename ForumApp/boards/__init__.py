from flask import Blueprint

bp = Blueprint('boards', __name__)

from ForumApp.boards import routes
