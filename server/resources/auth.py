from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token

from models import db
from models.user import User, Admin, Client, UserRole

class Register(Resource):
    def post(self):
        data=request.get_json()
        email = data.get('email')
        if not email:
            return {'message': 'Email is required'}, 400

        if User.query.filter_by(email=email).first():
            return {'message': 'User already exists'}, 400

        role = data.get('role')
        if role == 'CLIENT':
            new_user=Client(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                id_number=data.get('id_number', ''),
                role=UserRole.CLIENT
            )
        elif role == 'ADMIN':
            new_user = Admin(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                department=data['department'],
                role= UserRole.ADMIN
            )
        else:
            return {'message': 'Invalid role specified'}, 400

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201
    
class Login(Resource):
    def post(self):
        data=request.get_json()
        user=User.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            access_token=create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401

