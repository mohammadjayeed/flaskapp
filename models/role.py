from db import db


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',  ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('role', uselist=False, cascade='delete, delete-orphan', single_parent=True))


