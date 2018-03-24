from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import jsonify
from api.utils import APIError
import os

UPLOAD_FOLDER = 'photos/'

app = Flask(__name__)

# Setup the SQL Alchmey extension
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/hangry"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # TODO: Change this!
jwt = JWTManager(app)

CORS(app)

from api import models

@app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

#from api.models import User
#
# import and register blueprints
from api.views import users
app.register_blueprint(users.mod)

from api.views import auth
app.register_blueprint(auth.mod)

from api.views import photos
app.register_blueprint(photos.mod)
#
#from api.views import maps
#app.register_blueprint(maps.mod)
#
#from api.views import stories
#app.register_blueprint(stories.mod)
#
#from api.views import POIS
#app.register_blueprint(POIS.mod)
#
#from api.views import auth
#app.register_blueprint(auth.mod)
