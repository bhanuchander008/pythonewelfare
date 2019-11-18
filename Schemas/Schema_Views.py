
from config import db,ma
from marshmallow.fields import Nested
from Models.Model_Views import Views


class ViewGetSchemas(ma.ModelSchema):
    class Meta:
        model = Views
        sqla_session = db.session
