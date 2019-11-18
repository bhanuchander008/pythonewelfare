from flask import request
from config import db
from flask_restful import Resource
from Models.Model_Global_Settings import Globalsettings
from Schemas.Schema_GlobalSetting import Global_Settings_Schemas

class GetUpdateDelete_GlobalSettings(Resource):
    def __init__(self):
        pass
    
    def get(self,id):
        try:
            global_settings = db.session.query(Globalsettings).filter(Globalsettings.id == id).first()
            if global_settings:
                schema = Global_Settings_Schemas()
                data = schema.dump(global_settings).data
                return ({"success": True, "data": data})
            else:
                return ({"success": False, "message": "no data found on this id"})
        except Exception as e:
            return({"success": False, "message": str(e)})
        
    def put(self,id):
        try:
            global_settings = db.session.query(Globalsettings).filter(Globalsettings.id==id).update(request.get_json())
            if global_settings:
                db.session.commit()
                global_data = db.session.query(Globalsettings).filter_by(id=id).one()
                schema = Global_Settings_Schemas()
                data =  schema.dump(global_data).data
                return({"success": True, "data": data})
            else:
                return({"success": False, "message": "Global Setting not updated"})
        except Exception as e:
            return({"success": False, "message": str(e)})
    
    def delete(self, id):
        try:
            global_settings = db.session.query(Globalsettings).filter(Globalsettings.id == id).first()
            if global_settings:
                db.session.delete(global_settings)
                db.session.commit()
                return({"success": True, "message": "Global Setting data deleted successfully"})
            else:
                return({"success": False, "message": "Global Setting data not deleted on this id"})
        except Exception as e:
            return({"success": False, "message": str(e)})
