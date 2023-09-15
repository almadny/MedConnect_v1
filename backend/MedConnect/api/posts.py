from app import db

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(15), nullable=True, index=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """ Defines the appointment object string representation """
        return f"Post('{self.id}': '{self.title}' '{self.category}' '{self.date_posted}')"
