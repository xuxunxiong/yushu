from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


def creat_app():
    app = Flask(__name__)

    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app


def register_blueprint(app):
    from .web.book import web
    app.register_blueprint(web)
