from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import auth, books, public
    app.register_blueprint(auth.bp)
    app.register_blueprint(books.bp)
    app.register_blueprint(public.bp)

    return app
