from flask import Flask
from flask_login import LoginManager

from config import Config
from ForumApp.extensions import db
from flask_httpauth import HTTPBasicAuth

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager = LoginManager(app)

    #Initialize Flask Extensions here
    db.init_app(app)

    #Register Blueprints here

    # Home page blueprint
    with app.app_context():

        # Main Blueprint
        from ForumApp.main import bp as main_bp
        app.register_blueprint(main_bp)

        # Authentication Blueprint
        from ForumApp.auth import bp as auth_bp
        app.register_blueprint(auth_bp)

        # Profile Blueprint
        from ForumApp.profile import bp as profile_bp
        app.register_blueprint(profile_bp)

    return app
