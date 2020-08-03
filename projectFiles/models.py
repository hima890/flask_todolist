# import all the packigs
from flask_sqlalchemy import SQLAlchemy
from projectFiles import db
from datetime import datetime
timeNow = datetime.now() # curtine time

#database tebals
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datePost = db.Column(db.DateTime, default=timeNow)
    content = db.Column(db.Text, nullable=False)

class Complated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datePost = db.Column(db.DateTime)
    content = db.Column(db.Text, nullable=False)


