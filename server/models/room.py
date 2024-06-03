from . import db, CheckConstraint, association_proxy, validates
# import logging
# from faker import Faker

# fake = Faker()
# logger = logging.getLogger(__name__)

class Room(db.Model):
    __tablename__= "rooms"
    id = db.Column(db.Integer, primary_key=True)
    room_number= db.Column(db.Integer, nullable=True)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)
    description = db.Column(db.Text, nullable=False) 
    image= db.Column(db.String(200), nullable=False)
  
    __table_args__ = (
        CheckConstraint(room_type.in_(["Single", "Double", "Suite", "Presidential", "Deluxe", "Superior"])),
    )      
       
    reviews= db.relationship('Review', backref= 'room')
    bookings= db.relationship('Booking', backref= 'rooms')

    bookings =association_proxy('bookings_model', 'bookings')

    @validates('price_per_night')
    def validate_price(self, key, price_per_night):
        if price_per_night <= 0:
            raise ValueError('Price must be an amount more than zero')
        return price_per_night

    @validates('availability')
    def validate_availability(self, key, value):
        if not isinstance(value, bool):
            raise ValueError('Availability must be True or False')
        return value

    # @validates('description')
    # def validate_description(self, key, value):
    #     if not (200<=len(value)<=500):
    #         raise ValueError("Description must be between 200 and 500 character long")
    #     return value
    
    # @staticmethod
    # def generate_fake_description():
    #     description = fake.paragraph(nb_sentences=5)  # Generate a paragraph of 5 sentences
    #     description_length = len(description)
    #     logger.debug(f"Generated description: {description}")
    #     logger.debug(f"Description length: {description_length}")
    #     return description[:500]  # Limit the description to 500 characters

    # def __init__(self, **kwargs):
    #     super(Room, self).__init__(**kwargs)
    #     if not self.description:
    #         self.description = Room.generate_fake_description()

    # @staticmethod
    # def generate_random_check_out_date(check_in_date):
    #     end_date = '+2w'
    #     logger.debug(f"Check-in date: {check_in_date}")
    #     logger.debug(f"End date: {end_date}")
    #     check_out_date = fake.date_between(start_date=check_in_date, end_date=end_date)
    #     logger.debug(f"Generated check-out date: {check_out_date}")
    #     return check_out_date