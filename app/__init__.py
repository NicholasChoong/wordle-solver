from flask import Flask
from app.auth import bp as auth_bp
from app.main import bp as main_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
