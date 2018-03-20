from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost:5432/hangry"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def get_users():
    try:
        users=User.query.all()
        ret = ""
        for user in users:
            ret += user.username + ", " + user.email + "\n\n"
        return ret
    except Exception as ex:
        return create_response(data={}, status=400, message=str(ex))


if __name__ == '__main__':
    app.run(debug=True)
