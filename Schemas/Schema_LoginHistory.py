from Models.Model_Login_History import Loginhistories
from config import ma, db

class Login_Histories_Schemas(ma.ModelSchema):
    class Meta:
        model = Loginhistories
        sqla_session = db.session
