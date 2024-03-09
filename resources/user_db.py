import json
from models import User
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from flask_jwt_extended import jwt_required


blp = Blueprint("db_users", __name__, description="Read Users")

@blp.route("/users/db")
class UserListView(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        users = User.query.all()
        if not users:
            abort(404, message="No users found.")
        return users
    
@blp.route("/users/db/<int:uid>")
class UserDetailView(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, uid):
        user = User.query.get_or_404(uid)
        return user
