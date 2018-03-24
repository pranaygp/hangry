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

mod = Blueprint('locations', __name__)

@mod.route('/locations', methods = ["GET"])
def get_all_locations():
    try:
        result = conn.execute("SELECT * FROM location")
        locations = []
        for row in result:
            location = {}
            location["location_id"] = row["location_id"]
            location["restaurant_id"] = row["restaurant_id"]
            location["address"] = row["address"]
            location["zipcode"] = row["zipcode"]
            location["city"] = row["city"]
            location["country"] = row["country"]
            location["latitude"] = row["latitude"]
            location["longitude"] = row["longitude"]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/location', methods = ["POST"])
def create_location():
    data = request.get_json()
    try:
        result = conn.execute("INSERT INTO location (restaurant_id, address, zipcode, city, country, latitude, longitude) VALUES ({0}, \'{1}\', \'{2}\', \'{3}\', \'{4}\', {5}, {6})".format(data["restaurant_id"], data["address"], data["zipcode"], data["city"], data["country"], data["latitude"], data["longitude"]))
        return jsonify({'status':'success', 'message' : 'Successfully added location!'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/restaurant/<restaurant_id>', methods = ["GET"])
def get_all_restaurant_locations(restaurant_id):
    try:
        result = conn.execute("SELECT * FROM location WHERE restaurant_id = {}".format(restaurant_id))
        locations = []
        for row in result:
            location = {}
            location["location_id"] = row["location_id"]
            location["restaurant_id"] = row["restaurant_id"]
            location["address"] = row["address"]
            location["zipcode"] = row["zipcode"]
            location["city"] = row["city"]
            location["country"] = row["country"]
            location["latitude"] = row["latitude"]
            location["longitude"] = row["longitude"]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/zipcode/<zipcode>', methods = ["GET"])
def get_all_zipcode_locations(zipcode):
    try:
        result = conn.execute("SELECT * FROM location WHERE zipcode = \'{}\'".format(zipcode))
        locations = []
        for row in result:
            location = {}
            location["location_id"] = row["location_id"]
            location["restaurant_id"] = row["restaurant_id"]
            location["address"] = row["address"]
            location["zipcode"] = row["zipcode"]
            location["city"] = row["city"]
            location["country"] = row["country"]
            location["latitude"] = row["latitude"]
            location["longitude"] = row["longitude"]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/locations/city/<city>', methods = ["GET"])
def get_all_city_locations(city):
    try:
        result = conn.execute("SELECT * FROM location WHERE city = \'{}\'".format(city))
        locations = []
        for row in result:
            location = {}
            location["location_id"] = row["location_id"]
            location["restaurant_id"] = row["restaurant_id"]
            location["address"] = row["address"]
            location["zipcode"] = row["zipcode"]
            location["city"] = row["city"]
            location["country"] = row["country"]
            location["latitude"] = row["latitude"]
            location["longitude"] = row["longitude"]
            locations.append(location)
        return jsonify({'status':'success', 'locations' : locations})
    except Exception as e:
        raise APIError(str(e))
