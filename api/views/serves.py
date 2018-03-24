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

mod = Blueprint('serves', __name__)

@mod.route('/serves/restaurant/<restaurant_id>', methods = ["GET"])
def get_all_cuisines_served_by_rest(restaurant_id):
    try:
        result = conn.execute("SELECT cuisine.cuisine_id, cuisine.cuisine_name FROM serves, cuisine WHERE restaurant_id = {} and serves.cuisine_id = cuisine.cuisine_id".format(restaurant_id))
        cuisines = []
        for row in result:
            cuisine = {'cuisine_id' : row["cuisine_id"], 'cuisine_name' : row["cuisine_name"]}
            cuisines.append(cuisine)
        return jsonify({'status' : 'success', 'restaurant_id' : restaurant_id, 'cuisines' : cuisines})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/serves/cuisine/<cuisine_id>', methods = ["GET"])
def get_all_restaurants_by_cuisine(cuisine_id):
    try:
        result = conn.execute("SELECT restaurant.restaurant_id, restaurant.restaurant_name FROM serves, restaurant WHERE cuisine_id = {} and serves.restaurant_id = restaurant.restaurant_id".format(cuisine_id))
        restaurants = []
        for row in result:
            restaurant = {'restaurant_id' : row["restaurant_id"], 'restaurant_name' : row["restaurant_name"]}
            restaurants.append(restaurant)
        return jsonify({'status' : 'success', 'cuisine_id' : cuisine_id, 'restaurants' : restaurants})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/serves', methods = ["POST"])
def create_serves_entry():
    data = request.get_json()
    try:
        result = conn.execute("INSERT INTO serves (cuisine_id, restaurant_id) VALUES ({0}, {1})".format(data["cuisine_id"], data["restaurant_id"]))
        return jsonify({'status' : 'success', 'message' : 'Created serves entry!'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/serves/<serves_id>', methods = ["DELETE"])
def delete_serves_entry(serves_id):
    try:
        result = conn.execute("DELETE FROM serves WHERE serves_id = {}".format(serves_id))
        search = conn.execute("SELECT * FROM serves WHERE serves_id = {}".format(serves_id)).first()
        if search is not None:
            return jsonify({'status' : 'failed', 'message' : 'Failed to delete serves entry'})
        return jsonify({'status' : 'success', 'message' : 'Successfully deleted serves entry.'})
    except Exception as e:
        raise APIError(str(e))
