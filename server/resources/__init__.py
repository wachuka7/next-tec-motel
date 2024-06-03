from flask_restful import Api, Resource
from flask import jsonify

class HomeResource(Resource):
    def get(self):
        return jsonify(message="Welcome to the Next Tec Motel API!")

def register_resources(app):
    from .auth import Register, Login
    from .user import AdminResource,AdminListResource, ClientResource, ClientListResource
    from .room import RoomResource, RoomListResource
    from .booking import BookingResource, BookingListResource
    from .review import ReviewResource, ReviewListResource

    api = Api(app)

    api.add_resource(HomeResource, '/')
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(AdminListResource, '/admin')
    api.add_resource(AdminResource, '/admin/<int:id>')
    api.add_resource(ClientListResource, '/users')
    api.add_resource(ClientResource, '/users/<int:id>')


    api.add_resource(RoomListResource, '/rooms')
    api.add_resource(RoomResource, '/rooms/<int:id>')

    api.add_resource(BookingListResource, '/bookings')
    api.add_resource(BookingResource, '/bookings/<int:id>')

    api.add_resource(ReviewListResource, '/reviews')
    api.add_resource(ReviewResource, '/reviews/<int:id>')
    