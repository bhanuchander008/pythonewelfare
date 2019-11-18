from config import ma,db
from Models.Model_Roles import Roles

class RoleSchema(ma.ModelSchema):
    class Meta():
        model = Roles
        sqla_session = db.session

        