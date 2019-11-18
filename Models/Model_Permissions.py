from config import db
import datetime

class Permissions(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    add = db.Column(db.Boolean, nullable=True)
    edit = db.Column(db.Boolean, nullable=True)
    read = db.Column(db.Boolean, nullable=True)
    viewId = db.Column(db.Integer, db.ForeignKey('views.id'), nullable=True)
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
