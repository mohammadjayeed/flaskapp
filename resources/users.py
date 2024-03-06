from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blue_print = Blueprint("users", __name__, description="CRUD users")

@blue_print.route("/users")
class users(MethodView):
    def get(self):
        return 'success'