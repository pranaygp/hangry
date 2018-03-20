from api import db

db.create_all()
db.session.commit()
