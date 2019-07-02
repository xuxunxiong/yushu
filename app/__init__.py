from flask import Flask
from app.models.base import db


def creat_app():
    app = Flask(__name__)

    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from .web.book import web
    app.register_blueprint(web)
