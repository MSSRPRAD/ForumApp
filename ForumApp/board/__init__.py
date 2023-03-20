from flask import Blueprint

bp = Blueprint('board', __name__)

from ForumApp.board import routes
