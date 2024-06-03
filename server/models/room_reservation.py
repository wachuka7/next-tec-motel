# from . import db

# class RoomReservation(db.Model):
#     __tablename__ = 'room_reservation'
#     booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), primary_key=True)
#     room_id = db.Column(db.Integer, db.ForeignKey('room_id'), primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user_id'), primary_key=True)

#     booking = db.relationship("Booking", back_populates="room_reservation")
#     room = db.relationship("Room", back_populates="room_reservation")
#     client = db.relationship("Client", back_populates="room_reservation")

#     __table_args__ = (
#         db.UniqueConstraint('booking_id', 'room_id', name='unique_booking_room'),
#     )