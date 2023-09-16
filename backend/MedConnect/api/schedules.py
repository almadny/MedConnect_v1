from app import db

class TimeSlots(db.Model):
    __tablename__ = 'timeslots'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    day_of_the_week = db.Column(db.String(10), nullable=False, default='Everyday')
    timeslots_appointment = db.relationship('Appointments', backref='timeslots')
    # frequency = once, twice, thrice, four times, five times, six times or daily

    def __repr__(self):
        """ Defines the available_time object string representation """
        return f"TimeSlot('{self.id}': '{self.doctor_id}' '{self.day_of_the_week}' '{self.start_time}' '{self.end_time}')"
