from flask import Flask
from config import Config

from .extensions import mongo, login_manager, bcrypt


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # Initialize plugins
    login_manager.init_app(app)
    mongo.init_app(app)
    bcrypt.init_app(app)

    # register blueprints
    with app.app_context():
        from .home import home
        from .login import login
        from .dashboard import dashboard
        from .sign_up import sign_up

        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(login.login_blueprint)
        app.register_blueprint(dashboard.dashboard_blueprint)
        app.register_blueprint(sign_up.sign_up_blueprint)
        return app
