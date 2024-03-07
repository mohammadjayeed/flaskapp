import json
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from models import User

blp_db = Blueprint("db_users", __name__, description="Read Users")


@blp_db.route("/users/db")
class UserListView(MethodView):

    @blp_db.response(200, UserSchema(many=True))
    def get(self):
        users = User.query.all()
        if not users:
            abort(404, message="No users found.")
        return users
    
@blp_db.route("/users/db/<string:uid>")
class UserDetailView(MethodView):

    @blp_db.response(200, UserSchema)
    def get(self, uid):
        user = User.query.get_or_404(uid)
        return user
