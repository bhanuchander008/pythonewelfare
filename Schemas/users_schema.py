from config import ma,db
from Models.Model_Users import Users
from Models.Model_Roles import Roles
from Schemas.roles_schema import RoleSchema
class UserSchema(ma.ModelSchema):
    Role_User = ma.Nested(RoleSchema)
    class Meta():
        model = Users
        # fields = ("roleId",)
        sqla_session = db.session

        