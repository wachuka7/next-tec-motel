from flask_restful import Resource, reqparse
from models import db
from models.user import User, UserRole
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

admin_parser = reqparse.RequestParser()
admin_parser.add_argument('username', required=True, help="Username cannot be blank!")
admin_parser.add_argument('email', required=True, help="Email cannot be blank!")
admin_parser.add_argument('password', required=True, help="Password cannot be blank!")
admin_parser.add_argument('department', required=True, help="Department cannot be blank!")

client_parser = reqparse.RequestParser()
client_parser.add_argument('username', required=True, help="Username cannot be blank!")
client_parser.add_argument('email', required=True, help="Email cannot be blank!")
client_parser.add_argument('password', required=True, help="Password cannot be blank!")
client_parser.add_argument('id_number', required=True, help="ID number cannot be blank!")

class AdminResource(Resource):
    @jwt_required()
    def get(self, id):
        admin = User.query.filter_by(id=id, role=UserRole.ADMIN).first_or_404()
        return {
            'id': admin.id,
            'username': admin.username,
            'email': admin.email,
            'department': admin.department
        }

    @jwt_required()
    def put(self, id):
        args = admin_parser.parse_args()
        admin = User.query.filter_by(id=id, role=UserRole.ADMIN).first_or_404()
        admin.username = args['username']
        admin.email = args['email']
        admin.department = args['department']
        if 'password' in args:
            admin.password_hash = generate_password_hash(args['password'])
        db.session.commit()
        return {'message': 'Admin updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        admin = User.query.filter_by(id=id, role=UserRole.ADMIN).first_or_404()
        db.session.delete(admin)
        db.session.commit()
        return {'message': 'Admin deleted successfully'}, 200

class ClientResource(Resource):
    @jwt_required()
    def get(self, id):
        client = User.query.filter_by(id=id, role=UserRole.CLIENT).first_or_404()
        return {
            'id': client.id,
            'username': client.username,
            'email': client.email,
            'id_number': client.id_number
        }

    @jwt_required()
    def put(self, id):
        args = client_parser.parse_args()
        client = User.query.filter_by(id=id, role=UserRole.CLIENT).first_or_404()
        client.username = args['username']
        client.email = args['email']
        client.id_number = args['id_number']
        if 'password' in args:
            client.password_hash = generate_password_hash(args['password'])
        db.session.commit()
        return {'message': 'Client updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        client = User.query.filter_by(id=id, role=UserRole.CLIENT).first_or_404()
        db.session.delete(client)
        db.session.commit()
        return {'message': 'Client deleted successfully'}, 200

class AdminListResource(Resource):
    @jwt_required()
    def get(self):
        admins = User.query.filter_by(role=UserRole.ADMIN).all()
        return [{
            'id': admin.id, 
            'username': admin.username, 
            'email': admin.email, 
            'department': admin.department
        } for admin in admins]

    # @jwt_required()
    # def post(self):
    #     args = admin_parser.parse_args()
    #     new_admin = User(
    #         username=args['username'],
    #         email=args['email'],
    #         password=generate_password_hash(args['password']),
    #         role=UserRole.ADMIN,
    #         department=args['department']
    #     )
    #     db.session.add(new_admin)
    #     db.session.commit()
    #     return {'message': 'Admin created successfully'}, 201

class ClientListResource(Resource):
    @jwt_required()
    def get(self):
        clients = User.query.filter_by(role=UserRole.CLIENT).all()
        return [{
            'id': client.id, 
            'username': client.username, 
            'email': client.email, 
            'id_number': client.id_number
            } for client in clients]

    # @jwt_required()
    # def post(self):
    #     args = client_parser.parse_args()
    #     new_client = User(
    #         username=args['username'],
    #         email=args['email'],
    #         password=generate_password_hash(args['password']),
    #         role=UserRole.CLIENT,
    #         id_number=args['id_number']
    #     )
    #     db.session.add(new_client)
    #     db.session.commit()
    #     return {'message': 'Client created successfully'}, 201