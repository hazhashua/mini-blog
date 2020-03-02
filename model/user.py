
from flask_sqlalchemy import SQLAlchemy
from view.views import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@47.92.202.163/blog'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return "UserL <%r>"%self.username


if __name__ == "__main__":
    db.create_all()
