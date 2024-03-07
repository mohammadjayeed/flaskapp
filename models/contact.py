from db import db

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    user = db.relationship('User', backref=db.backref('contact', uselist=False, cascade='delete, delete-orphan', single_parent=True))
