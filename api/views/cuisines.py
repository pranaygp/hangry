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

mod = Blueprint('cuisines', __name__)

@mod.route('/cuisines', methods = ["GET"])
def get_all_cuisines():
    try:
        result = conn.execute("SELECT * FROM cuisine")
        cuisines = []
        for row in result:
            cuisine = {}
            cuisine["cuisine_id"] = row["cuisine_id"]
            cuisine["cuisine_name"] = row["cuisine_name"]
            cuisines.append(cuisine)
        return jsonify({'status' : 'success', 'cuisines' : cuisines})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/cuisine', methods = ["POST"])
def create_cuisine():
    data = request.get_json()
    try:
        result = conn.execute("INSERT INTO cuisine (cuisine_name) VALUES (\'{}\')".format(data["cuisine_name"]))
        return jsonify({'status' : 'success', 'message' : 'Successfully created cuisine!'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/cuisine/<cuisine_id>', methods = ["GET", "DELETE"])
def get_or_delete_cuisine(cuisine_id):
    try:
        if request.method == "GET":
            result = conn.execute("SELECT * FROM cuisine WHERE cuisine_id = {}".format(cuisine_id))
            row = result.first()
            if row is not None:
                return jsonify({'status' : 'success', 'cuisine_id' : row["cuisine_id"], 'cuisine_name' : row["cuisine_name"]})
            return jsonify({'status': 'failed', 'message' : 'No corresponding cuisine found'})
        elif request.method == "DELETE":
            result = conn.execute("DELETE FROM cuisine WHERE cuisine_id = {}".format(cuisine_id))
            select = conn.execute("SELECT * FROM cuisine WHERE cuisine_id = {}".format(cuisine_id))
            if select.first() is None:
                return jsonify({'status' : 'success', 'message' : 'Successfully deleted cuisine!'})
            return jsonify({'status' : 'failed', 'message' : 'Failed to delete cuisine (might not exist?).'})
    except Exception as e:
        raise APIError(str(e))
