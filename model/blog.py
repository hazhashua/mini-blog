from view.views import app
from flask_sqlalchemy import SQLAlchemy
from model.user import db

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@47.92.202.163/blog'
# db = SQLAlchemy(app)

class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    # user_id = db.Column(db.Integer)
    blog_name = db.Column(db.String(60))
    blog_content = db.Column(db.Text())
    create_date = db.Column(db.Date())
    modify_date = db.Column(db.Date())
    reference_count = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id, blog_name, create_date, modify_date, blog_content=""):
        self.user_id = user_id
        self.blog_name = blog_name
        self.blog_content = blog_content
        self.create_date = create_date
        self.modify_date = modify_date


    def __repr__(self):
        return "Blog: <%d:%r>"%(self.user_id, self.blog_name)


if __name__ == "__main__":
    db.create_all()