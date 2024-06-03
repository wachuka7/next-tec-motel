from . import db, UserRole, validates
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)

    reviews= db.relationship('Review', backref= 'user')

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role = role

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
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    id_number = db.Column(db.Integer, nullable=False)

    def __init__(self, username, email, password, role, id_number):
        super().__init__(username, email, password, role)
        self.id_number = id_number

    @validates('id_number')
    def validate_id_number(self, key, id_number):
        if not id_number:
            raise ValueError('ID number is required')
        return id_number


class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    department = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password, role, department):
        super().__init__(username, email, password, role)
        self.department = department

    @validates('department')
    def validate_department(self, key, department):
        if not department:
            raise ValueError('Department is required')
        return department