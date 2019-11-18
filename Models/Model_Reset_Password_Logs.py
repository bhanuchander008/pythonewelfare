from config import db
import datetime
class Resetpasswordlogs(db.Model):
    __tablename__ = "resetpasswordlogs"
    id = db.Column(db.Integer, primary_key=True)
    lastPassword = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
