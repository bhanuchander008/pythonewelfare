from datetime import datetime
from flask import make_response,request
from config import * 
from Models.Model_Users import Users
from Schemas.users_schema import UserSchema
from flask_restful import Resource,reqparse


# users post and get all users call
class User_Post(Resource):
    def __init__(self,*args,**kwargs):
        pass

    #users get call
    def get(self):
        try:
            user=db.session.query(Users).order_by(Users.id).all()
            if user:
                user_schema = UserSchema(many=True)
                data = user_schema.dump(user).data
                return {"success":True,"message":data}
            else:
                return{"success":False,"message":"No data is available on roles"}
        except Exception as e:
            return e
    
    # Users Post call
    def post(self):
        try:
            get_data=request.get_json()
            if get_data['email']:
                if '@' in get_data['email']:
                    schema = UserSchema()
                    # print(schema)
                    # new_role = schema.load(dit, session=db.session).data
                    new_user = schema.load(get_data, session=db.session).data
                    # print(new_user)
                    db.session.add(new_user)
                    db.session.commit()
                    data = schema.dump(new_user).data
                    return {"success":True,"message":data}
                else:
                    return {"success":False,"message":"Invalid Email Id"}
            schema = UserSchema()
            new_user = schema.load(get_data, session=db.session).data
            db.session.add(new_user)
            db.session.commit()
            data = schema.dump(new_user).data
            return {"success":True,"message":data}
        except Exception as e:
            return e


# Get Post and Delete call based on role id 
class User_by_id(Resource):
    def __init__(self):
        pass
    # Role get call based on id
    def get(self,id):
        try:
            get_user=db.session.query(Users).filter(Users.id==id).first()
            if get_user:
                user_schema = UserSchema()
                data = user_schema.dump(get_user).data
                return {"success":True,"message":data}
            else:
                return {"success":False,"message":"No data is found on this id"}
        except Exception as e:
            return e


    # Roles update call based on id
    def put(self,id):
        try:
            obj=db.session.query(Users).filter(Users.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                abc=db.session.query(Users).filter_by(id=id).one()
                schema = UserSchema()
                data = schema.dump(abc).data
                return {"success":True,"message":data}
            else:
                return {"success":False,"Meassage":"No data is found on this id"}
        except Exception as e:
            return e


    # Roles delete call based on id
    def delete(self,id):
        try:
            obj=db.session.query(Users).filter(Users.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return {"success":True,"message":"Role deleted successfully"}
            else:
                return {"success":False,"message":"No data is found on this id"}
        except Exception as e:
            return e 
