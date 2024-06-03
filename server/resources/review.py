from flask_restful import Resource, reqparse
from models import db, Review
from flask_jwt_extended import jwt_required
from flask import jsonify

review_parser = reqparse.RequestParser()
review_parser.add_argument('user_id', type=int, required=True, help="User ID cannot be blank!")
review_parser.add_argument('room_id', type=int, required=True, help="Room ID cannot be blank!")
review_parser.add_argument('rating', type=int, required=True, help="Rating cannot be blank!")
review_parser.add_argument('review_text', required=False)

class ReviewResource(Resource):
    @jwt_required()
    def get(self, id):
        review = Review.query.get_or_404(id)
        return {
            'id': review.id,
            'user_id': review.user_id,
            'room_id': review.room_id,
            'rating': review.rating,
            'review_text': review.review_text,
            'date_submitted': review.date_submitted
        }

    @jwt_required()
    def put(self, id):
        args = review_parser.parse_args()
        review = Review.query.get_or_404(id)
        review.user_id = args['user_id']
        review.room_id = args['room_id']
        review.rating = args['rating']
        review.review_text = args.get('review_text', review.review_text)
        db.session.commit()
        return {'message': 'Review updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        review = Review.query.get_or_404(id)
        db.session.delete(review)
        db.session.commit()
        return {'message': 'Review deleted successfully'}, 200

class ReviewListResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return [{
            'id': review.id, 
            'user_id': review.user_id, 
            'room_id': review.room_id, 
            'rating': review.rating, 
            'review_text': review.review_text, 
            'date_submitted': review.date_submitted.strftime('%Y-%m-%d %H:%M:%S')
            } 
            for review in reviews]

    @jwt_required()
    def post(self):
        args = review_parser.parse_args()
        new_review = Review(
            user_id=args['user_id'],
            room_id=args['room_id'],
            rating=args['rating'],
            review_text=args.get('review_text')
        )
        db.session.add(new_review)
        db.session.commit()
        return {'message': 'Review created successfully'}, 201
