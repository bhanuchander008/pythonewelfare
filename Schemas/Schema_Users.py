from config import ma, db
from Models.Model_Users import Users
from Models.Model_Roles import Roles

class UserSchema(ma.ModelSchema):
  class Meta():
      model = Users
      sqla_session = db.session
