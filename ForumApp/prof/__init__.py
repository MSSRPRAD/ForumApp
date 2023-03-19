from flask import Blueprint

bp = Blueprint('prof', __name__)

from ForumApp.prof import routes
