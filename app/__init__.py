from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    jwt = JWTManager(app)
    from .models.book import Book
    from .models.user import User
    from .routes import auth, books, public

    app.register_blueprint(auth.bp)
    app.register_blueprint(books.bp)
    app.register_blueprint(public.bp)

    return app
