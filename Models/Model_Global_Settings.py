from config import db
import datetime


class Globalsettings(db.Model):
    __tablename__ = "globalsettings"
    id = db.Column(db.Integer, primary_key=True)
    linkExpiry = db.Column(db.Integer, nullable=True)
    invalidloginAttempts = db.Column(db.Integer, nullable=True)
    freezeTime = db.Column(db.Integer, nullable=True)
    passwordExpirydays = db.Column(db.Integer, nullable=True)
    expiryIntimationDays = db.Column(db.Integer, nullable=True)
    invalidloginAttemptsInTime = db.Column(db.Integer, nullable=True)
    sessionTime = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
