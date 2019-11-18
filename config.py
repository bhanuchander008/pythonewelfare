from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Welcome@123@104.199.146.29/ewelfare_python"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
ma = Marshmallow(app)
db = SQLAlchemy(app)
db.init_app(app)
