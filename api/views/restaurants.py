import json
from api import app
from api import db
from api.models import Restaurant
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify

engine = db.engine
conn = engine.connect()

mod = Blueprint('restaurants', __name__)

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@mod.route('/restaurants', methods=["GET"])
def get_all_restaurants():
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"restaurant\"")
            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = row[key]
                restaurants.append(restaurants)
            return jsonify({'restaurants' : restaurants})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurants requires GET request"})

@mod.route('/restaurant', methods=["POST"])
def create_restaurant():
    if request.method == "POST":
        try:
            data = request.get_json()
            add_restaurant = ("INSERT INTO restaurant " +
               "(restaurant_id, restaurant_name) " +
               "VALUES ('{0}', '{1}').format(data['restaurant_id'], data['restaurant_name'])
            result = conn.execute(add_restaurant)
            return jsonify({'status' : 'success', 'message' : 'Created new restaurant!'})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurant requires GET or POST request"})

@mod.route('/restaurant/id/<restaurant_id>', methods=["GET", "DELETE"])
def get_restaurant_by_id(restaurant_id):
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant_id = {}".format(restaurant_id))
            row = result.first()
            if row != None:
                restaurant = {"restaurant_id" : row["restaurant_id"], "restaurant_name" : row["restaurant_name"]}
                return jsonify({'status' : 'success', 'restaurant' : restaurant})
            return jsonify({'status' : 'failed', 'message' : 'No restaurant record found!'})
        except Exception as e:
            raise APIError(str(e))
    elif request.method == "DELETE":
        try:
            result = conn.execute("DELETE FROM \"restaurant\" WHERE restaurant_id = {}".format(restaurant_id))
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant_id = {}".format(restaurant_id))
            row = result.first()
            if row != None:
                return jsonify({"status" : "failed", "message" : "Failed to delete restaurant."})
            return jsonify({"status" : "success", "message" : "Successfully deleted restaurant!"})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurant/id requires GET or POST request"})

@mod.route('/restaurant/name/<restaurant_name>', methods=["GET", "DELETE"])
def get_restaurant_by_name(restaurant_name):
    if request.method == "GET": #return all instances
        try:
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant_name = \'{}\'".format(restaurant_name))
            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = row[key]
                restaurants.append(restaurants)
            if len(restaurants) > 0: return jsonify({'restaurants' : restaurants})
            else: return jsonify({'status' : 'failed', 'message' : 'No restaurant record found!'})
        except Exception as e:
            raise APIError(str(e))
    elif request.method == "DELETE":
        try:
            result = conn.execute("DELETE FROM \"restaurant\" WHERE restaurant_name = \'{}\'".format(restaurant_name))
            result = conn.execute("SELECT * FROM \"restaurant\" WHERE restaurant_name = \'{}\'".format(restaurant_name))
            row = result.first()
            if row != None:
                return jsonify({"status" : "failed", "message" : "Failed to delete restaurant."})
            return jsonify({"status" : "success", "message" : "Successfully deleted all instances of restaurant!"})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /restaurant/restaurant_name requires GET or POST request"})
