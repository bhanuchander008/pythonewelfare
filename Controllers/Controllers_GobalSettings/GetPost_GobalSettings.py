from flask import request
from config import db
from flask_restful import Resource
from Models.Model_Global_Settings import Globalsettings
from Schemas.Schema_GlobalSetting import Global_Settings_Schemas

class GetPostGlobalSettings(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            global_settings = db.session.query(Globalsettings).order_by(Globalsettings.id).all()
            if global_settings:
                schema = Global_Settings_Schemas(many=True)
                data = schema.dump(global_settings).data
                return ({"success": True, "data": data})
            else:
                return({"success": False, "message": "No data is available for Global Settings"})
        except Exception as e:
            return({"success": False, "message": str(e)})

    def post(self):
        try:
            global_settings = request.get_json()
            schema = Global_Settings_Schemas()
            new_record = schema.load(global_settings, session=db.session).data
            db.session.add(new_record)
            db.session.commit()
            data = schema.dump(new_record).data
            return ({"success": True, "data": data})
        except Exception as e:
            return({"success": False, "message": str(e)})
