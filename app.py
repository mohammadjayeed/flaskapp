import os
import models
from flask import Flask
from flask_smorest import Api
from db import db
from flask_jwt_extended import JWTManager
from resources.user_db_view import blp as UserDatabaseBlueprint
from resources.user_json_view import blp as UserFileBasedBlueprint 
from resources.user_json_child_view import blp as UserFileBasedBlueprintChild
from resources.admin_view import blp as AdminUserBlueprint
from resources.search_view import blp as SearchBlueprint
from flask_swagger_ui import get_swaggerui_blueprint

from dotenv import load_dotenv

def create_app(db_url=None):

    app = Flask(__name__)
    load_dotenv()
    app.json.sort_keys = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    # app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    # app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    SWAGGER_URL = '/swagger-ui'
    API_URL = '/static/swagger_doc.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL

    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL",  'sqlite:///data.db' )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_DB_SEEDS_PATH"] = os.path.join(os.getcwd(), 'seeds.py')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)

    app.config["JWT_SECRET_KEY"] =  os.getenv("JWT_SECRET")
    jwt = JWTManager(app)

    api.register_blueprint(AdminUserBlueprint)
    api.register_blueprint(UserDatabaseBlueprint)
    api.register_blueprint(UserFileBasedBlueprint)
    api.register_blueprint(UserFileBasedBlueprintChild, url_prefix='/users/json')
    api.register_blueprint(SearchBlueprint)

    return app