from flask_restful import Resource, reqparse
from models import db, Booking
from flask_jwt_extended import jwt_required
from flask import jsonify

booking_parser = reqparse.RequestParser()
booking_parser.add_argument('user_id', type=int, required=True, help="User ID cannot be blank!")
booking_parser.add_argument('room_id', type=int, required=True, help="Room ID cannot be blank!")
booking_parser.add_argument('check_in_date', required=True, help="Check-in date cannot be blank!")
booking_parser.add_argument('check_out_date', required=True, help="Check-out date cannot be blank!")
booking_parser.add_argument('total_price', type=float, required=True, help="Total price cannot be blank!")

class BookingResource(Resource):
    @jwt_required()
    def get(self, id):
        booking = Booking.query.get_or_404(id)
        return {
            'id': booking.id,
            'user_id': booking.user_id,
            'room_id': booking.room_id,
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date,
            'total_price': booking.total_price
        }

    @jwt_required()
    def put(self, id):
        args = booking_parser.parse_args()
        booking = Booking.query.get_or_404(id)
        booking.user_id = args['user_id']
        booking.room_id = args['room_id']
        booking.check_in_date = args['check_in_date']
        booking.check_out_date = args['check_out_date']
        booking.total_price = args['total_price']
        db.session.commit()
        return {'message': 'Booking updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        booking = Booking.query.get_or_404(id)
        db.session.delete(booking)
        db.session.commit()
        return {'message': 'Booking deleted successfully'}, 200

class BookingListResource(Resource):
    @jwt_required()
    def get(self):
        bookings = Booking.query.all()
        bookings_data= [{
            'id': booking.id, 
            'user_id': booking.user_id, 
            'room_id': booking.room_id, 
            'check_in_date': booking.check_in_date, 
            'check_out_date': booking.check_out_date, 
            'total_price': booking.total_price
            } 
            for booking in bookings]
        return jsonify(bookings_data)
    

    @jwt_required()
    def post(self):
        args = booking_parser.parse_args()
        new_booking = Booking(
            user_id=args['user_id'],
            room_id=args['room_id'],
            check_in_date=args['check_in_date'],
            check_out_date=args['check_out_date'],
            total_price=args['total_price']
        )
        db.session.add(new_booking)
        db.session.commit()
        return {'message': 'Booking created successfully'}, 201
