from flask import Flask
from . import auth, public, config, blog
from .extensions import db, migrate, login_manager, csrf_protect, mail
from . import models


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevConfig)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(auth.views.bp)
    app.register_blueprint(public.views.bp)
    app.register_blueprint(blog.views.bp)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
