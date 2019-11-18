from datetime import datetime
from flask import make_response,abort,request
from Models.Model_Views import Permissions
from Schemas.Schema_Permissions import PermissionGetSchemas,PermissionGetSchema
from config import *
from flask_restful import reqparse, abort, Api, Resource
import os



class GetUpdateDeletePermission(Resource):
    def __init__(self):
        pass
    def get(self,id):
        try:
            permission=db.session.query(Permissions).filter(Permissions.id==id).first()
            if permission:
                permission_schema = PermissionGetSchemas()
                data = permission_schema.dump(permission).data
                return({"success":True,"data":data})
            else:
                return({"success":False,"message": "Permission not found"})
        except Exception as e:
            return({"success":False,"message":str(e)})

    def put(self,id):
        try:
            obj=db.session.query(Permissions).filter(Permissions.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                permission_obj=db.session.query(Permissions).filter_by(id=id).one()
                schema = PermissionGetSchemas()
                data = schema.dump(permission_obj).data
                return({"success":True,"data":data})
            else:
                return({"success":False,"message": "permission not updated"}  )
        except Exception as e:
            return({"success":False,"message":str(e)})


    def delete(self,id):
        try:
            obj=db.session.query(Permissions).filter(Permissions.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return({"success":True,"message":"succesffully deleted"})
            else:
                return({"success":False,"message": "Permissions doesnot deleted "})
        except Exception as e:
            return({"success":False,"message":str(e)})
