import json
from api import app
from api import db
from api.models import User
from api.utils import APIError
from flask import Blueprint, request
from flask import jsonify

engine = db.engine
conn = engine.connect()

mod = Blueprint('users', __name__)

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@mod.route('/users', methods=["GET"])
def get_all_users():
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"user\"")
            users  = []
            for row in result:
                user = {}
                for key in row.keys():
                    user[key] = row[key]
                users.append(user)
            return jsonify({'users' : users})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /users requires GET request"})

@mod.route('/user', methods=["POST"])
def create_user():
    if request.method == "POST":
        try:
            data = request.get_json()
            result = conn.execute("INSERT INTO \"user\" (email, username, password, name, latitude, longitude) VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', {4}, {5})".format(data["email"], data["username"], data["password"], data["name"], data["latitude"], data["longitude"]))
            return jsonify({'status' : 'success', 'message' : 'Created new user!'})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /user requires GET or POST request"})

@mod.route('/user/id/<user_id>', methods=["GET", "DELETE"])
def get_user_by_id(user_id):
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"user\" WHERE user_id = {}".format(user_id))
            row = result.first()
            if row != None:
                user = {"user_id" : row["user_id"], "email" : row["email"], "username" : row["username"], "password" : row["password"], "name" : row["name"], "latitude" : row["latitude"], "longitude" : row["longitude"]}
                return jsonify({'status' : 'success', 'user' : user})
            return jsonify({'status' : 'failed', 'message' : 'No user record found!'})
        except Exception as e:
            raise APIError(str(e))
    elif request.method == "DELETE":
        try:
            result = conn.execute("DELETE FROM \"user\" WHERE user_id = {}".format(user_id))
            result = conn.execute("SELECT * FROM \"user\" WHERE user_id = {}".format(user_id))
            row = result.first()
            if row != None:
                return jsonify({"status" : "failed", "message" : "Failed to delete user."})
            return jsonify({"status" : "success", "message" : "Successfully deleted user!"})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /user requires GET or POST request"})

@mod.route('/user/username/<username>', methods=["GET", "DELETE"])
def get_user_by_username(username):
    if request.method == "GET":
        try:
            result = conn.execute("SELECT * FROM \"user\" WHERE username = \'{}\'".format(username))
            row = result.first()
            if row != None:
                user = {"user_id" : row["user_id"], "email" : row["email"], "username" : row["username"], "password" : row["password"], "name" : row["name"], "latitude" : row["latitude"], "longitude" : row["longitude"]}
                return jsonify({'status' : 'success', 'user' : user})
            return jsonify({'status' : 'failed', 'message' : 'No user record found!'})
        except Exception as e:
            raise APIError(str(e))
    elif request.method == "DELETE":
        try:
            result = conn.execute("DELETE FROM \"user\" WHERE username = \'{}\'".format(username))
            result = conn.execute("SELECT * FROM \"user\" WHERE username = \'{}\'".format(username))
            row = result.first()
            if row != None:
                return jsonify({"status" : "failed", "message" : "Failed to delete user."})
            return jsonify({"status" : "success", "message" : "Successfully deleted user!"})
        except Exception as e:
            raise APIError(str(e))
    else:
        return jsonify({'status' : 'failed', 'message' : "Endpoint /user requires GET or POST request"})
