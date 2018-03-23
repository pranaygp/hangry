from api import app, db
from flask import Blueprint, request
from api.models import User
from flask import jsonify
from flask_jwt_extended import create_access_token
import json

mod = Blueprint('auth', __name__)

conn = db.engine.connect()

# '''
# Flask Login requires ORM to handle all the authentication/session business for us,
# so we have to use ORM instead of raw SQL here. However, here is the equivalent SQL
# query:

# SELECT * FROM user WHERE user.user_id = user_id
# '''

@app.route('/signup', methods = ['POST'])
def signup_user():
    data = request.get_json()
    username_search = conn.execute("SELECT * FROM \"user\" WHERE username = \'{}\'".format(data["username"]))
    email_search = conn.execute("SELECT * FROM \"user\" WHERE email = \'{}\'".format(data["email"]))
    if username_search.first() != None and email_search.first() != None:
        data = request.get_json()
        result = conn.execute("INSERT INTO \"user\" (email, username, password, name, latitude, longitude) VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', {4}, {5})".format(data["email"], data["username"], data["password"], data["name"], data["latitude"], data["longitude"]))
        access_token = create_access_token(identity=data["username"])
        return jsonify({'status' : 'success', 'message' : 'Created new user!', token: access_token})
    return jsonify({'status':'failed', 'message': 'Username or email already exist'})

@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    # print(data["username"])
    # print(data["password"])
    user = db.session.query(User).filter_by(username = data["username"]).first()
    if user is not None:
        if user.password == data["password"]:
            db.session.commit()
             # Identity can be any data that is json serializable
            access_token = create_access_token(identity=data["username"])
            return jsonify({'status':'success', 'username': data["username"], "token": access_token})
        else:
            return jsonify({'status':'failed', 'message': 'Wrong username and/or password'})

    return jsonify({'status':'failed', 'message': 'Wrong username and/or password'})

# @app.route('/logout', methods = ['GET'])
# @jwt_required
# def logout():
#     db.session.commit()
#     return jsonify({'status': 'suceeded', 'message': "logged out"})
