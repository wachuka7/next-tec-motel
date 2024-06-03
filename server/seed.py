from datetime import date, datetime
from app import create_app
from models import db
from models.user import User, UserRole, Admin, Client
from models.room import Room
# from models.room_reservation import RoomReservation
from models.booking import Booking
from models.review import Review

app = create_app()

with app.app_context():
    # Drop all tables and create them
    db.drop_all()
    db.create_all()

    # Create admin user
    admin_data = {
        "username": "admin",
        "email": "admin@example.com",
        "password": "adminpassword",
        "role": UserRole.ADMIN,
        "department": "Administration"
    }
    admin = Admin(**admin_data)
    db.session.add(admin)
    db.session.commit()

    # Create clients
    clients_data = [
        {
            "username": "user1",
            "email": "user1@example.com",
            "password": "user1password",
            "role": UserRole.CLIENT,
            "id_number": 1
        },
        {
            "username": "user2",
            "email": "user2@example.com",
            "password": "user2password",
            "role": UserRole.CLIENT,
            "id_number": 2
        },
        # Add more clients here
    ]
    for client_data in clients_data:
        client = Client(**client_data)
        db.session.add(client)
    db.session.commit()

    # Create rooms
    rooms_data = [
        {
            "room_number": 1,
            "room_type": "Single",
            "price_per_night": 100,
            "availability": True,
            "description": "Room description for room 1",
            "image": "https://example.com/room1.jpg"
        },
        {
            "room_number": 2,
            "room_type": "Double",
            "price_per_night": 110,
            "availability": True,
            "description": "Room description for room 2",
            "image": "https://example.com/room2.jpg"
        },
        # Add more rooms here
    ]
    for room_data in rooms_data:
        room = Room(**room_data)
        db.session.add(room)
    db.session.commit()

    # Create bookings
    bookings_data = [
        {
            "user_id": 1,
            "room_id": 1,
            "check_in_date": datetime.strptime("2024-06-03", "%Y-%m-%d").date(),
            "check_out_date": datetime.strptime("2024-06-04", "%Y-%m-%d").date(),
            "total_price": 200
        },
        {
            "user_id": 2,
            "room_id": 2,
            "check_in_date": datetime.strptime("2024-06-03", "%Y-%m-%d").date(),
            "check_out_date": datetime.strptime("2024-06-05", "%Y-%m-%d").date(),
            "total_price": 220
        },
        # Add more bookings here
    ]
    for booking_data in bookings_data:
        booking = Booking(**booking_data)
        db.session.add(booking)
    db.session.commit()

    # Create reviews
    reviews_data = [
        {
            "user_id": 1,
            "room_id": 1,
            "rating": 5,
            "review_text": "Great room!"
        },
        {
            "user_id": 2,
            "room_id": 2,
            "rating": 4,
            "review_text": "Nice stay."
        },
        # Add more reviews here
    ]
    for review_data in reviews_data:
        review = Review(**review_data)
        db.session.add(review)
    db.session.commit()

    print("Database seeded successfully!")
