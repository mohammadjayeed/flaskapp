from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import User, Contact, Role
from flask_jwt_extended import jwt_required
from sqlalchemy import or_
from marshmallow import Schema, fields
from schemas import SearchSchema


blp = Blueprint("Search",__name__, description="Search From Database by first_name | company | country | Role Name" )


@blp.route("/search")
class SearchView(MethodView):
    
    @jwt_required()
    @blp.arguments(SearchSchema)
    @blp.response(200)
    def post(self, data):
        
        query = db.session.query(User).\
        join(Contact).\
        join(Role).\
        filter(
            or_(
                User.first_name.contains(data['keyword']),
                User.company.contains(data['keyword']),
                Contact.country.contains(data['keyword']),
                Role.name.contains(data['keyword'])
            )
        ).all()
    
        results = []

        for item in query:
            i = {}
            i['id'] = item.id
            i['first_name'] = item.first_name
            i['last_name'] = item.last_name
            i['active'] = item.active
            i['company'] = item.company
            i['country'] = item.contact.country
            i['role'] = item.role.name
            i['company'] = item.company
            results.append(i)
        
        return results