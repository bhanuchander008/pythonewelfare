from Models.Model_Reset_Password_Logs import Resetpasswordlogs
from config import ma,db


class Reset_PasswordLogs_Schemas(ma.ModelSchema):
    class Meta:
        model = Resetpasswordlogs
        sqla_session = db.session
