from config import db
from sqlalchemy.orm import validates
from Models.Model_Reset_Password_Logs import Resetpasswordlogs
from Models.Model_Global_Settings import Globalsettings
from Models.Model_Login_History import Loginhistories
import datetime

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    prefix = db.Column(db.String(255), nullable=True)
    group = db.Column(db.String(255), nullable=True)
    username = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    mobileNumber = db.Column(db.String(255), nullable=True)
    mobileNumberExtension = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    citizenId = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    groupName = db.Column(db.String(255), nullable=True)
    verified = db.Column(db.Boolean(), nullable=True)
    token = db.Column(db.String(255), nullable=True)
    lockedOut = db.Column(db.Boolean(), nullable=True)
    passwordExpired = db.Column(db.Boolean(), nullable=True)
    officeNumber = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)

    


    Reset_Password_logs = db.relationship("Resetpasswordlogs", backref=db.backref("User_ResetPasswordLogs"))
    Global_Settings = db.relationship("Globalsettings", backref=db.backref("User_Globalsettings"))
    Login_Histories = db.relationship("Loginhistories", backref=db.backref("User_Loginhistories"))
