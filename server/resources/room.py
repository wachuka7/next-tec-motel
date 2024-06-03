from flask_restful import Resource, reqparse
from models import db, Room
from flask_jwt_extended import jwt_required

room_parser = reqparse.RequestParser()
room_parser.add_argument('room_number', type=int, required=True, help="Room number cannot be blank!")
room_parser.add_argument('room_type', required=True, help="Room type cannot be blank!")
room_parser.add_argument('price_per_night', type=float, required=True, help="Price per night cannot be blank!")
room_parser.add_argument('availability', type=bool, required=True, help="Availability cannot be blank!")
room_parser.add_argument('description', required=True, help="Description cannot be blank!")
room_parser.add_argument('image', required=True, help="Image cannot be blank!")

class RoomResource(Resource):
    @jwt_required()
    def get(self, id):
        room = Room.query.get_or_404(id)
        return {
            'id': room.id,
            'room_number': room.room_number,
            'room_type': room.room_type,
            'price_per_night': room.price_per_night,
            'availability': room.availability,
            'description': room.description,
            'image': room.image
        }

    @jwt_required()
    def put(self, id):
        args = room_parser.parse_args()
        room = Room.query.get_or_404(id)
        room.room_number = args['room_number']
        room.room_type = args['room_type']
        room.price_per_night = args['price_per_night']
        room.availability = args['availability']
        room.description = args['description']
        room.image = args['image']
        db.session.commit()
        return {'message': 'Room updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        room = Room.query.get_or_404(id)
        db.session.delete(room)
        db.session.commit()
        return {'message': 'Room deleted successfully'}, 200

class RoomListResource(Resource):
    def get(self):
        rooms = Room.query.all()
        return [{'id': room.id, 'room_number': room.room_number, 'room_type': room.room_type, 'price_per_night': room.price_per_night, 'availability': room.availability, 'description': room.description, 'image': room.image} for room in rooms]

    @jwt_required()
    def post(self):
        args = room_parser.parse_args()
        new_room = Room(
            room_number=args['room_number'],
            room_type=args['room_type'],
            price_per_night=args['price_per_night'],
            availability=args['availability'],
            description=args['description'],
            image=args['image']
        )
        db.session.add(new_room)
        db.session.commit()
        return {'message': 'Room created successfully'}, 201
