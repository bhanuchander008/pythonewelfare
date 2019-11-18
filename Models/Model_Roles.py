from config import db
from Models.Model_Users import Users
from Models.Model_Permissions import Permissions
import datetime

class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    role_type = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    User = db.relationship("Users", backref=db.backref("Role_User"))
    Permission = db.relationship("Permissions", backref=db.backref("Role_Permission"))
