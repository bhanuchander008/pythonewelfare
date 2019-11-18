from datetime import datetime
from flask import make_response,request
from config import * 
from Models.Model_Roles import Roles
from Schemas.roles_schema import RoleSchema
from flask_restful import Resource,reqparse



# Post and Get call of Roles Model
class Post_Roles(Resource):
    def __init__(self):
        pass
    # Roles Get call
    def get(self):
        try:
            role=db.session.query(Roles).order_by(Roles.id).all()
            if role:
                role_schema = RoleSchema(many=True)
                data = role_schema.dump(role).data
                return {"success":True,"message":data}
            else:
                return{"success":False,"message":"No data is available on roles"}
        except Exception as e:
            return e

    # Roles Post call
    def post(self):
        try:
            get_data = request.get_json()
            name = get_data['name']
            dit = {key:value for key,value in get_data.items()}
            existing_role = (Roles.query.filter(Roles.name == name).one_or_none())
            if existing_role is None:
                schema = RoleSchema()
                new_role = schema.load(dit, session=db.session).data
                db.session.add(new_role)
                db.session.commit()
                data = schema.dump(new_role).data
                return {"success":True,"message":data}
            else:
                return {"success":False,"message":"Role name exists already"}
        except Exception as e:
            return e


# Get Post and Delete call based on role id 
class Role_by_id(Resource):
    def __init__(self):
        pass
    # Role get call based on id
    def get(self,id):
        try:
            get_role=db.session.query(Roles).filter(Roles.id==id).first()
            if get_role:
                role_schema = RoleSchema()
                data = role_schema.dump(get_role).data
                return {"success":True,"message":data}
            else:
                return {"success":False,"message":"No data is found on this id"}
        except Exception as e:
            return e


    # Roles update call based on id
    def put(self,id):
        try:
            obj=db.session.query(Roles).filter(Roles.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                abc=db.session.query(Roles).filter_by(id=id).one()
                schema = RoleSchema()
                data = schema.dump(abc).data
                return {"success":True,"message":data}
            else:
                return {"success":False,"Meassage":"No data is found on this id"}
        except Exception as e:
            return e


    # Roles delete call based on id
    def delete(self,id):
        try:
            obj=db.session.query(Roles).filter(Roles.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return("Role deleted successfully")
            else:
                return("No data is found on this id")
        except Exception as e:
            return e        



