import os
from flask import Flask
from flask_smorest import Api
from db import db
import models
from resources.users_db import blp_db as UserBlueprint
from resources.users_json import blp_json as UserJSONBlueprint

def create_app(db_url=None):

    app = Flask(__name__)

    app.json.sort_keys = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "User Data REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)


    api.register_blueprint(UserBlueprint)
    api.register_blueprint(UserJSONBlueprint)

    return app