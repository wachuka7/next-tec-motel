import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import Config
from models.user import User


load_dotenv()

app= Flask(__name__)
CORS(app)
db= SQLAlchemy()
migrate= Migrate()
jwt=JWTManager()

def create_app(app):
    
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

@jwt.unauthorized_loader
def custom_unauthorized_response(_err):
    return {"message": "Missing Authorization Header"}, 401

@jwt.invalid_token_loader
def custom_invalid_token_response(_err):
    return {"message": "Invalid token"}, 422