from . import db, validates
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum

class UserRole(Enum):
    ADMIN = 'admin'
    CLIENT = 'client'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)
    department = db.Column(db.String(120), nullable=True)  
    id_number = db.Column(db.String(120), nullable=True) 

    reviews= db.relationship('Review', backref= 'user')
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    def __init__(self, username, email, password, role, department=None, id_number=None):
        self.username = username
        self.email = email
        self.set_password(password)
        self.role = role
        self.department = department
        self.id_number = id_number

    def set_password(self, password):
        self.password_hash=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email is required')
        return email


class Client(User):
    __tablename__='clients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }

    def __init__(self, username, email, password, id_number, role):
        super().__init__(username, email, password, role)
        self.id_number = id_number

    @validates('id_number')
    def validate_id_number(self, key, id_number):
        if not id_number:
            raise ValueError('ID number is required')
        return id_number


class Admin(User):
    __tablename__='admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, username, email, password, department,role):
        super().__init__(username, email, password, role)
        self.department = department

    @validates('department')
    def validate_department(self, key, department):
        if not department:
            raise ValueError('Department is required')
        return department