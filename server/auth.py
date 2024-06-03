from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token

from app import db
from models.user import User

class Register(Resource):
    def post(self):
        data=request.get_json()
        if User.query.filter_by(email=data['email']).first():
            return{'message': 'User already exists'}, 400
        
        new_user=User(
            username=data['username'],
            email=data['email']
        )
        new_user.set_password(data['password'])

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201
    
class Login(Resource):
    def post(self):
        data=request.get_json()
        user=user.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            access_token=create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Inavalid credentials'}, 401

