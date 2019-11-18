from config import db
import datetime


class Loginhistories(db.Model):
    __tablename__ = "loginhistories"
    id = db.Column(db.Integer, primary_key=True)
    loginDate = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable = True)
    status = db.Column(db.String(255), nullable=True)
    ipaddress = db.Column(db.String(255), nullable=True)
    loggedOutTime = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable = True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
