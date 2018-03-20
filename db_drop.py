from api import db

db.drop_all()
db.session.commit()
