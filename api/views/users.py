import json
from api import app
from api import db
from api.models import User
from flask import Blueprint, request
from flask import jsonify

#engine = db.engine
#connection = engine.connect()

mod = Blueprint('users', __name__)

@mod.route('/users')
def get_all_users():
    users = db.session.query(User).all()
    users_arr = []
    for user in users:
        user_dict = {}
        user_dict["email"] = user.email
        user_dict["username"] = user.username
        user_dict["password"] = user.password
        user_dict["name"] = user.name
        user_dict["latitude"] = user.latitude
        user_dict["longitude"] = user.longitude
        users_arr.append(user_dict)
    return jsonify({'users' : users_arr})

# WTF. Can't get the raw SQL to work, it connects to the default postgres db instead of hangry.
'''
@mod.route('/users')
def get_all_users():
    result = db.engine.execute("SELECT * FROM user")
    users  = []
    for row in result:
        user = {}
        for key in row.keys():
            user[key] = row[key]
        users.append(user)
    return jsonify({'users' : users})
'''
