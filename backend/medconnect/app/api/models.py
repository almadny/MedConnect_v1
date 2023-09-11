from flask-sqlalchemy import SQLAlchemy
from app import db

class Patients(db.Model):
    id = db.Column(String)
