import json, time
from api import app
from api import db
from api.models import Checkins
from api.utils import APIError
from sqlalchemy import text
from flask import Blueprint, request
from flask import jsonify
from flask_login import LoginManager, login_required, login_user, logout_user

engine = db.engine
conn = engine.connect()

mod = Blueprint('checkins', __name__)

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@mod.route('/checkin', methods=["GET"])
def get_all_checkins():
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"checkins\"")
            checkins  = []
            for row in result:
                checkin = {}
                for key in row.keys():
                    checkin[key] = row[key]
                checkins.append(checkin)
            return jsonify({'checkins' : checkins})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /checkin requires GET request"})

@mod.route('/checkin', methods=["POST"])
def create_checkin():
    if request.method == "POST":
        try:
            data = request.get_json()
            add_checkin = text("INSERT INTO checkins (user_id, location_id, timestamp) VALUES({0}, {1}, '{2}')"
            .format(data["user_id"], data["location_id"], time.strftime('%Y-%m-%d %H:%M:%S')))

            result = conn.execute(add_checkin)
            return jsonify({'status' : 'success', 'message' : 'Created new checkin!'})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /checkin requires GET or POST request"})
