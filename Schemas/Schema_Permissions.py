
from config import db,ma
from marshmallow.fields import Nested
from Models.Model_Views import Permissions
from Schemas.Schema_Roles import RoleSchema
from Schemas.Schema_Views import ViewGetSchemas

class PermissionGetSchemas(ma.ModelSchema):

    class Meta:
        model = Permissions
        sqla_session = db.session


class PermissionGetSchema(ma.ModelSchema):

    class Meta:
        model = Permissions
        fields = ("id","add","edit","read","roleId","viewId")
        sqla_session = db.session




class PermissionSchema(ma.ModelSchema):
    Role_Permission= ma.Nested(RoleSchema)
    view_permission = ma.Nested(ViewGetSchemas)
    class Meta:
        model = Permissions
        fields = ("id","add","edit","read","Role_Permission","view_permission")
        sqla_session = db.session
