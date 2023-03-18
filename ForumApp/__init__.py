from flask import Flask

from config import Config
from ForumApp.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    #Initialize Flask Extensions here

    #Register Blueprints here

    # Home page blueprint
    from ForumApp.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Authentication Blueprint
    from ForumApp.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
