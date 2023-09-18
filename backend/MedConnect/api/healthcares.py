from api import db
from datetime import datetime

class Healthcares(db.Model):
    __tablename__ = 'healthcares'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    address = db.Column(db.String(32), nullable=False, unique=True)
    contact_number = db.Column(db.String(32), nullable=False, unique=True)
    doctor = db.relationship('Doctors', backref='healthcares')

    def __repr__(self):
        """ Defines the Healthcare object string representation """
        return f"Healthcare('{self.id}': '{self.name}')"
