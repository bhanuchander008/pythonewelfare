from datetime import datetime
from flask import make_response,abort,request
from Models.Model_Views import Views
from Schemas.Schema_Views import ViewGetSchemas
from config import *
from flask_restful import reqparse, abort, Api, Resource
import os





class GetPostViews(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            view=db.session.query(Views).order_by(Views.id).all()
            if view:
                view_schema = ViewGetSchemas(many=True)
                data = view_schema.dump(view).data
                return({"success":True,"data":data})
            else:
                return({"success":False,"message": "views not found"})
        except Exception as e:
           return({"success":False,"message":str(e)})


    def post(self):
        try:
            da = request.get_json()
            name = da['name']
            existing_view = (Views.query.filter(Views.name == name).one_or_none())
            if existing_view is None:
                schema = ViewGetSchemas()
                new_view = schema.load(da, session=db.session).data
                db.session.add(new_view)
                db.session.commit()
                data = schema.dump(new_view).data
                return({"success":True,"data":data})
            else:
                return("view name exists already")
        except Exception as e:
            return({"success":False,"message":str(e)})
