import json
import datetime
from api import app
from api import db
#from api.models import restaurant, location, cuisine, rating, checkin
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify

engine = db.engine
conn = engine.connect()

mod = Blueprint('leaderboard', __name__)

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@mod.route('/leaderboard/hot/<user_id>', methods=["GET"])
def get_hot_restaurants(user_id):
    if request.method == "GET":
        try:
            data = request.get_json()
            get_hot_restaurants = """
                                    SELECT close_restaurants.restaurant_id, close_restaurants.restaurant_name, AVG(rating.rating), COUNT(checkins)
                                    FROM restaurant, rating, checkins,
                                        (SELECT restaurant.restaurant_id, restaurant.restaurant_name
                                        FROM location, restaurant, "user"
                                        WHERE "user".user_id = {0} AND
                                            restaurant.restaurant_id = location.restaurant_id AND
                                            (location.latitude < 1.1 * "user".latitude OR
                                            location.latitude > 0.9 * "user".latitude) AND
                                            (location.longitude < 1.1 * "user".longitude OR
                                            location.longitude > 0.9 * "user".longitude)
                                        ) AS close_restaurants
                                    WHERE close_restaurants.restaurant_id = rating.restaurant_id AND
	                                      close_restaurants.restaurant_id = checkins.restaurant_id AND
	                                      checkins.timestamp > '{1}'
                                    GROUP BY close_restaurants.restaurant_id, close_restaurants.restaurant_name
                                  """.format(user_id, datetime.datetime.now() - datetime.timedelta(days=14))

            result = conn.execute(get_hot_restaurants)

            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = row[key]
                restaurants.append(restaurant)
            return jsonify({'restaurants' : restaurants, 'status' : 'success'})
        except Exception as e:
            raise APIError(str(e))

    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /hot requires GET request"})
