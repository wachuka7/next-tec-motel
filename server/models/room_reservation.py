from . import db

class RoomReservation(db.Model):
    __tablename__ = 'room_reservation'
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    booking = db.relationship("Booking", backref="room_reservation")
    room = db.relationship("Room", backref="room_reservation")
    user = db.relationship("User", backref="room_reservation")

    __table_args__ = (
        db.UniqueConstraint('booking_id', 'room_id', name='unique_booking_room'),
    )