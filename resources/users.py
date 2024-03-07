from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from models import User

blue_print = Blueprint("users", __name__, description="CRUD users")

@blue_print.route("/users/db")
class UserListView(MethodView):

    @blue_print.response(200, UserSchema(many=True))
    def get(self):
        users = User.query.all()
        if not users:
            abort(404, message="No users found.")
        return users
    
@blue_print.route("/users/db/<string:uid>")
class UserDetailView(MethodView):

    @blue_print.response(200, UserSchema)
    def get(self, uid):
        user = User.query.get_or_404(uid)
        return user
    