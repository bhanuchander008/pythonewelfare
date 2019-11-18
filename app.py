from flask import Flask
from flask_restful import Api
from config import *
app = Flask(__name__)
api = Api(app)

#----------------------------Roles--------------------------------------------
from Controllers.Roles.roles import Post_Roles,Role_by_id
api.add_resource(Post_Roles,'/addroles')
api.add_resource(Role_by_id,'/rolebyid/<int:id>')
#--------------------------users---------------------------------
from Controllers.Users.users import User_Post,User_by_id
api.add_resource(User_Post,'/addusers')
api.add_resource(User_by_id,'/userbyid/<int:id>')





from Controllers.Views.postview import GetPostViews
from Controllers.Views.getupdateview import GetUpdateDeleteViews

api.add_resource(GetPostViews, '/api/getpostview')
api.add_resource(GetUpdateDeleteViews, '/api/getupdatedview/<int:id>')


from Controllers.Permissions.postpermissions import GetPostPermissions
from Controllers.Permissions.getupdatepermission import GetUpdateDeletePermission

api.add_resource(GetPostPermissions, '/api/getpostpermissions')
api.add_resource(GetUpdateDeletePermission, '/api/getupdatepermission/<int:id>')

from Controllers.Controllers_GobalSettings.GetPost_GobalSettings import GetPostGlobalSettings
from Controllers.Controllers_GobalSettings.GetUpdateDelete_GobalSettings import GetUpdateDelete_GlobalSettings

api.add_resource(GetPostGlobalSettings, '/getpostglobalsettings')
api.add_resource(GetUpdateDelete_GlobalSettings, '/getupdatedeleteglobalsettings/<int:id>')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
