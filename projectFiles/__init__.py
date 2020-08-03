# import all the packigs
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from projectFiles.config import Config


# Database launch and the migration
db = SQLAlchemy()
migrate = Migrate()

# the main app function
def create_app(config_class=Config):
    # the Flask class instaince 
    app = Flask(__name__)
    # import the configration from config file
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    # create the database
    with app.app_context():
        from projectFiles import models
        db.create_all()
    # register the main blueprint
    from projectFiles.main.routes import home_page
    app.register_blueprint(home_page)
    return app