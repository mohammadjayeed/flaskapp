from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import User, Contact, Role
from flask_jwt_extended import jwt_required
from sqlalchemy import or_
from marshmallow import Schema, fields
from schemas import SearchSchema


blp = Blueprint("Search",__name__, description="Search by first_name | company | country | Role Name" )


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
                User.first_name.contains(data['term']),
                User.company.contains(data['term']),
                Contact.country.contains(data['term']),
                Role.name.contains(data['term'])
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