import json
from api import app
from api import db
from api.models import Restaurant, Location, Cuisine, Rating, Checkin
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

@mod.route('/hot', methods=["GET"])
def get_hot_restaurants(user_id):
    if request.method == "GET":
        try:
            data = request.get_json()
            get_hot_restaurants = """
                                    SELECT restaurant.restaruant_id, restaurant.restaurant_name, AVG(rating), COUNT(checkin)
                                    FROM \"rating\", \"checkin\"
                                        (SELECT *
                                        FROM \"location\", \"restaurant\",
                                            (SELECT *
                                             FROM \"user\"
                                             WHERE user_id = {}.format(user_id)
                                            ) AS curr_user
                                        WHERE restaurant.restaurant_id = location.restaurant_id AND
                                            location.latitude < 1.001 * curr_user.latitude AND
                                            location.latitude > 0.999 * curr_user.latitude AND
                                            location.longitude < 1.001 * curr_user.longitude AND
                                            location.longitude > 0.999 * curr_user.longitude
                                        ) AS close_restaurants
                                    WHERE close_restaurants.restaurant_id = rating.restaurant_id AND
	                                      close_restaurants.restaurant_id = checkin.restaurant_id AND
	                                      checkin.timestamp > datetime.datetime.now() - timedelta(days=14)
                                  """

            result = conn.execute(get_hot_restaurants)

            restaurants  = []
            for row in result:
                restaurant = {}
                for key in row.keys():
                    restaurant[key] = row[key]
                restaurants.append(restaurant)
            return jsonify({'restaurants' : restaurants})
        except Exception as e:
            raise APIError(str(e))
            
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /hot requires GET request"})
