
import os

class Config:
    SECRET_KEY= os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= os.getenv('DATABASE_URL', 'sqlite:///finance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    JWT_SECRET_KEY= os.getenv('JWT_SECRET_KEY')
