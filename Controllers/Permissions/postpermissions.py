from datetime import datetime
from flask import make_response,abort,request
from Models.Model_Views import Permissions
from Schemas.Schema_Permissions import PermissionGetSchemas,PermissionGetSchema,PermissionSchema
from config import *
from flask_restful import reqparse, abort, Api, Resource
import os





class GetPostPermissions(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            permission=db.session.query(Permissions).order_by(Permissions.id).all()
            if permission:
                permission_schema = PermissionSchema(many=True)
                data = permission_schema.dump(permission).data
                return({"success":True,"data":data})
            else:
                return({"success":False,"message": "permission not found"})
        except Exception as e:
           return({"success":False,"message":str(e)})


    def post(self):
        try:
            da = request.get_json()
            print("da",da)
            schema = PermissionGetSchema()
            new_view = schema.load(da, session=db.session).data
            db.session.add(new_view)
            db.session.commit()
            data = schema.dump(new_view).data
            return({"success":True,"data":data})
        except Exception as e:
            return({"success":False,"message":str(e)})
