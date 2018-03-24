import os
from api import app
from api import db
from api.models import User
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify
from flask_login import LoginManager, login_required, login_user, logout_user

engine = db.engine
conn = engine.connect()

mod = Blueprint('ratings', __name__)

@mod.route('/ratings/user/<user_id>', methods = ["GET"])
def get_all_user_ratings(user_id):
    try:
        result = conn.execute("SELECT * FROM rating WHERE user_id = {}".format(user_id))
        user_ratings = []
        for row in result:
            rating = {}
            rating["rating_id"] = row["rating_id"]
            rating["user_id"] = row["user_id"]
            rating["restaurant_id"] = row["restaurant_id"]
            rating["rating"] = row["rating"]
            user_ratings.append(rating)
        return jsonify({'status':'success', 'ratings':user_ratings})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/ratings/restaurant/<restaurant_id>', methods = ["GET"])
def get_all_restaurant_ratings(restaurant_id):
    try:
        result = conn.execute("SELECT * FROM rating WHERE restaurant_id = {}".format(restaurant_id))
        restaurant_ratings = []
        for row in result:
            rating = {}
            rating["rating_id"] = row["rating_id"]
            rating["user_id"] = row["user_id"]
            rating["restaurant_id"] = row["restaurant_id"]
            rating["rating"] = row["rating"]
            restaurant_ratings.append(rating)
        return jsonify({'status':'success', 'ratings':restaurant_ratings})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/ratings/<rating_id>', methods = ["GET", "DELETE"])
def get_or_delete_rating(rating_id):
    try:
        if request.method == "GET":
            result = conn.execute("SELECT * FROM rating WHERE rating_id = {}".format(rating_id))
            row = result.first()
            if row is not None:
                rating = {}
                rating["rating_id"] = row["rating_id"]
                rating["user_id"] = row["user_id"]
                rating["restaurant_id"] = row["restaurant_id"]
                rating["rating"] = row["rating"]
                return jsonify({'status' : 'success', 'rating' : rating})
            return jsonify({'status' : 'failed', 'message' : 'Rating not found.'})
        elif request.method == "DELETE":
            result = conn.execute("DELETE FROM rating WHERE rating_id = {}".format(rating_id))
            select = conn.execute("SELECT * FROM rating WHERE rating_id = {}".format(rating_id))
            if select.first() is None:
                return jsonify({'status' : 'success', 'message' : 'Successfully deleted rating!'})
            return jsonify({'status' : 'failed', 'message' : 'Failed to delete rating (might not exist?).'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/ratings/<rating_id>/<rating>', methods = ["PUT"])
def update_rating(rating_id, rating):
    try:
        result = conn.execute("UPDATE rating SET rating = {0} WHERE rating_id = {1}".format(rating, rating_id))
        return jsonify({'status' : 'success', 'message' : 'Successfully updated rating!'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/ratings', methods = ["POST"])
def create_rating():
    data = request.get_json()
    try:
        result = conn.execute("INSERT INTO rating (user_id, restaurant_id, rating) VALUES ({0}, {1}, {2})".format(data["user_id"], data["restaurant_id"], data["rating"]))
        return jsonify({'status' : 'success', 'message' : 'Successfully created rating!'})
    except Exception as e:
        raise APIError(str(e))
