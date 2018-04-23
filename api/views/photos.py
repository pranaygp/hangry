import os
import uuid
import time
from api import app
from api import db
from api.models import User
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify
from flask_login import LoginManager, login_required, login_user, logout_user

engine = db.engine
conn = engine.connect()

mod = Blueprint('photos', __name__)

@mod.route('/photos/restaurant/<restaurant_id>', methods = ["GET"])
def get_restaurant_photos(restaurant_id):
    try:
        result = conn.execute("SELECT * FROM photo WHERE restaurant_id = {} ORDER BY timestamp DESC".format(restaurant_id))
        photos = []
        for row in result:
            photo = {}
            photo["user_id"] = row["user_id"]
            photo["restaurant_id"] = row["restaurant_id"]
            photo["photo_path"] = row["photo_path"]
            photo["timestamp"] = row["timestamp"]
            photo["photo_id"] = row["photo_id"]
            photos.append(photo)
        if len(photos) == 0:
            return jsonify({'status' : 'failed', 'message' : 'Failed to find photo.'})
        return jsonify({'status' : 'success', 'photos' : photos})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/photos/user/<user_id>', methods = ["GET"])
def get_user_photos(user_id):
    try:
        result = conn.execute("SELECT * FROM photo WHERE user_id = {} ORDER BY timestamp DESC".format(user_id))
        photos = []
        for row in result:
            photo = {}
            photo["user_id"] = row["user_id"]
            photo["restaurant_id"] = row["restaurant_id"]
            photo["photo_path"] = row["photo_path"]
            photo["timestamp"] = row["timestamp"]
            photos.append(photo)
        if len(photos) == 0:
            return jsonify({'status' : 'failed', 'message' : 'Failed to find photo.'})
        return jsonify({'status' : 'success', 'photos' : photos})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/photos', methods = ["POST"])
def upload_photo():
    try:
        data = request.get_json()
        result = conn.execute("INSERT INTO photo (user_id, restaurant_id, photo_path, timestamp) VALUES ({0}, {1}, \'{2}\', \'{3}\')".format(data["user_id"], data["restaurant_id"], data["image_url"], time.strftime('%Y-%m-%d %H:%M:%S')))
        return jsonify({'status' : 'success', 'message' : 'Successfully uploaded image!'})
    except Exception as e:
        raise APIError(str(e))

@mod.route('/photos/<photo_id>', methods = ["DELETE"])
def delete_photo(photo_id):
    try:
        deletion = conn.execute("DELETE FROM photo WHERE photo_id = {}".format(photo_id))
        check = conn.execute("SELECT * FROM photo WHERE photo_id = {}".format(photo_id)).first()
        if check is not None:
            return jsonify({'status' : 'failed', 'message' : 'Failed to delete photo'})
        return jsonify({'status' : 'success', 'message' : 'Successfully deleted photo!'})
    except Exception as e:
        raise APIError(str(e))
