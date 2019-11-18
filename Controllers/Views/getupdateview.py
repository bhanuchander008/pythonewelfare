from datetime import datetime
from flask import make_response,abort,request
from Models.Model_Views import Views
from Schemas.Schema_Views import ViewGetSchemas
from config import *
from flask_restful import reqparse, abort, Api, Resource
import os



class GetUpdateDeleteViews(Resource):
    def __init__(self):
        pass
    def get(self,id):
        try:
            view=db.session.query(Views).filter(Views.id==id).first()

            if view:
                view_schema = ViewGetSchemas()
                data = view_schema.dump(view).data
                return({"success":True,"data":data})
            else:
                return({"success":False,"message": "Views not found"})
        except Exception as e:
            return({"success":False,"message":str(e)})

    def put(self,id):
        try:
            obj=db.session.query(Views).filter(Views.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                view_obj=db.session.query(Views).filter_by(id=id).one()
                schema = ViewGetSchemas()
                data = schema.dump(view_obj).data
                return({"success":True,"data":data})
            else:
                return({"success":False,"message": "views not updated"}  )
        except Exception as e:
            return({"success":False,"message":str(e)})


    def delete(self,id):
        try:
            obj=db.session.query(Views).filter(Views.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return({"success":True,"message":"succesffully deleted"})
            else:
                return({"success":False,"message": "view doesnot deleted "})
        except Exception as e:
            return({"success":False,"message":str(e)})
