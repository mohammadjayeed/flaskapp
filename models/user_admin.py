from db import db

class AdminUserModel(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(60), unique = True, nullable = False)
    password = db.Column(db.String(), unique = True, nullable = False)