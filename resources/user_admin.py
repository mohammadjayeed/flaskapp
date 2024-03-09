import bcrypt
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token
from flask import make_response, jsonify
from db import db
from models import AdminUserModel
from schemas import AdminUserSchema
from datetime import timedelta
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash


blp = Blueprint("Admin",__name__, description="Authenticate Users" )

@blp.route("/register")
class AdminUserRegister(MethodView):

    @blp.arguments(AdminUserSchema)
    def post(self, data):
        if AdminUserModel.query.filter(AdminUserModel.username == data["username"]).first():
            return make_response(jsonify({'message': 'same name already exists'}), 422)
        

        passw = generate_password_hash(data["password"], method='pbkdf2:sha256')

        user = AdminUserModel(
            
            username=data["username"], password=passw)
            
        db.session.add(user)
        db.session.commit()

        return make_response(jsonify({'message': 'User Created Successfully'}), 201)


@blp.route("/admin/<int:id>")
class AdminUserGetDelete(MethodView):

    @jwt_required()
    @blp.response(200,AdminUserSchema)
    def get(self, id):
        user = AdminUserModel.query.get_or_404(id)
        return user
    
    @jwt_required()
    def delete(self, id):
        user = AdminUserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User Deleted'}), 200)
    

@blp.route("/login")
class AdminUserLogin(MethodView):
    @blp.arguments(AdminUserSchema)
    def post(self, data):
        user = AdminUserModel.query.filter(
            AdminUserModel.username == data["username"]
        ).first()

        matched = check_password_hash(user.password, data["password"])
        if user and matched:
            expires = timedelta(minutes=45)
            access_token = create_access_token(identity=user.id, expires_delta=expires) # {'user':user.id, 'username':user.username}
            return make_response(jsonify({'access_token': access_token}), 200)

        return make_response(jsonify({'message': 'Invalid Credentials'}), 401)