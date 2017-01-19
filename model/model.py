from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    name = db.Column(db.String(64))
    sex = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(512), nullable=True)
    school_id = db.Column(db.Integer)
    grade_id = db.Column(db.Integer, nullable=True)
    class_id = db.Column(db.Integer, nullable=True)
    activated = db.Column(db.Integer)
    class_no = db.Column(db.Integer, nullable=True)
    is_main = db.Column(db.Integer, nullable=True)
