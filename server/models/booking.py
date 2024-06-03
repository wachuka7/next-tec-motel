from . import db, validates


class Booking(db.Model):
    __tablename__='bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    rooms= db.relationship('Room', secondary='room_reservation', backref='bookings')

@validates('check_in_date', 'check_out_date')
def validate_dates(self, key, date):
    if key== 'check_in_date' and self.check_out_date and date>=self.check_out_date:
        raise ValueError('Invalid Input: check_in date must be before the check_out date')
    elif key== 'check_out_date' and self.check_in_date and date<=self.check_in_date:
        raise ValueError("Invalid Input: Check-out date must be after the check-in date")