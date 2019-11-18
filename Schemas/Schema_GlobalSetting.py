from Models.Model_Global_Settings import Globalsettings
from config import ma, db
from Schemas.Schema_Users import UserSchema

class Global_Settings_Schemas(ma.ModelSchema):
    class Meta:
        model = Globalsettings
        sqla_session = db.session

