from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["SECRET_KEY"] = "dev-key"  # temporary
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    from .admin import init_admin

    app.register_blueprint(main)
    init_admin(app)

    return app
