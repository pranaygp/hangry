from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager, login_required
import os

app = Flask(__name__)
app.secret_key = 'verysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/hangry"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from api import models
#
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = "login"
#
#
#from api.models import User
#
#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.filter_by(id = user_id).first()
#
# import and register blueprints
from api.views import users
app.register_blueprint(users.mod)

from api.views import auth
app.register_blueprint(auth.mod)
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
