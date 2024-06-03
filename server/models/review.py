from . import db, validates, func


class Review(db.Model):
    __tablename__= "reviews"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    rating= db.Column(db.Integer, nullable=False)
    review_text= db.Column(db.String(300), nullable= True)    
    date_submitted= db.Column(db.DateTime, nullable= False, default=func.now())

    @validates('rating')
    def validate_rating(self, key, rating):
        if rating not in [1, 2, 3, 4, 5]:
            raise ValueError("Rating must be between 1 and 5")
        return rating