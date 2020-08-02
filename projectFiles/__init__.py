from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from projectFiles.config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from projectFiles import models
        db.create_all()

    from projectFiles.main.routes import home_page
    app.register_blueprint(home_page)
    return app