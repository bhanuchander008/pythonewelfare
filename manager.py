import os
from Models.Model_Roles import Roles
from Models.Model_Users import Users
from Models.Model_Views import Views
from Models.Model_Permissions import Permissions
from Models.Model_Reset_Password_Logs import Resetpasswordlogs
from Models.Model_Global_Settings import Globalsettings
from Models.Model_Login_History import Loginhistories

from flask_restful import Api
from config import db, app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

app.app_context().push()

db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
   manager.run()
