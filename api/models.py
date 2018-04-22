from api import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def get_id(self):
        return str(self.user_id).encode()

class Restaurant(db.Model):
    restaurant_id = db.Column(db.Integer, unique=True, primary_key=True)
    restaurant_name = db.Column(db.String(80))

class Cuisine(db.Model):
    cuisine_id = db.Column(db.Integer, unique=True, primary_key=True)
    cuisine_name = db.Column(db.String(80))

class Photo(db.Model):
    photo_id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)
    photo_path = db.Column(db.String(140), unique=True, nullable=False)

class Rating(db.Model):
    rating_id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)

class Location(db.Model):
    location_id = db.Column(db.Integer, unique=True, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)
    address = db.Column(db.String(100))
    zipcode = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

class Serves(db.Model):
    serves_id = db.Column(db.Integer, unique=True, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisine.cuisine_id"), nullable=False)

class Checkins(db.Model):
    user_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    checkin_id = db.Column(db.Integer, unique=True, primary_key=True)
    timestamp = db.Column(db.DateTime)
    # , db.ForeignKey("user.user_id")
    #  db.ForeignKey("restaurant.restaurant_id"),