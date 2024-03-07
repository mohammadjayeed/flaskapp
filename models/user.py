from db import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)
    company = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(1), nullable=False)



