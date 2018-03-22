from api import app, db, login_manager
from flask import Blueprint, request
from api.models import User
from flask import jsonify
from flask_login import LoginManager, login_required, login_user, logout_user

mod = Blueprint('auth', __name__)

conn = db.engine.connect()

'''
Flask Login requires ORM to handle all the authentication/session business for us,
so we have to use ORM instead of raw SQL here. However, here is the equivalent SQL
query:

SELECT * FROM user WHERE user.user_id = user_id
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id = int(user_id)).first()

@app.route('/signup', methods = ['POST'])
def signup_user():
    data = request.get_json()
    username_search = conn.execute("SELECT * FROM \"user\" WHERE username = \'{}\'".format(data["username"]))
    email_search = conn.execute("SELECT * FROM \"user\" WHERE email = \'{}\'".format(data["email"]))
    if username_search.first() != None and email_search.first() != None:
        data = request.get_json()
        result = conn.execute("INSERT INTO \"user\" (email, username, password, name, latitude, longitude) VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', {4}, {5})".format(data["email"], data["username"], data["password"], data["name"], data["latitude"], data["longitude"]))
        return jsonify({'status' : 'success', 'message' : 'Created new user!'})
    return jsonify({'status':'failed', 'message': 'Username or email already exist'})

@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    user = db.session.query(User).filter_by(username = data["username"]).first()
    if user is not None:
        if user.password == data["password"]:
            login_user(user)
            db.session.commit()
            return jsonify({'status':'success', 'username': "User %s successfully logged in!" % data["username"]})
        else:
            return jsonify({'status':'failed', 'message': 'Wrong username and/or password'})

    return jsonify({'status':'failed', 'message': 'Wrong username and/or password'})

@login_required
@app.route('/logout', methods = ['POST'])
def logout():
    logout_user()
    db.session.commit()
    return jsonify({'status': 'suceeded', 'message': "logged out"})
