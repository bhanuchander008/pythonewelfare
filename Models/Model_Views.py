from config import db
from Models.Model_Permissions import Permissions
import datetime

class Views(db.Model):
    __tablename__ = 'views'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    alias = db.Column(db.String(255), nullable=True)
    globalAdd = db.Column(db.Boolean, nullable=True)
    globalRead = db.Column(db.Boolean, nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    Permission = db.relationship("Permissions", backref=db.backref("view_permission"))
