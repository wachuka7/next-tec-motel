from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, CheckConstraint, func
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declared_attr
from enum import Enum

metadata= MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db= SQLAlchemy(metadata=metadata)

class UserRole(Enum):
    ADMIN = 'admin'
    CLIENT = 'client'

from .user import User
from .room import Room
from .booking import Booking
from .review import Review
# from .room_reservation import RoomReservation

