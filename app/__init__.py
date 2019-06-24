from flask import Flask


def creat_app():
    app = Flask(__name__)

    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from .web.book import web
    app.register_blueprint(web)
