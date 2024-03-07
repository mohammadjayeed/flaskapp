import json
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SimpleContactSchema, SimpleRoleSchema, UserPostSchemaJSON, UserGetSchemaJSON
from models import User

blp_json = Blueprint("json_user",__name__, description="CRUD Users")

@blp_json.route("/users/json")
class UserListCreateViewJSON(MethodView):

    def get(self):


        with open('sample.json', 'r') as file:
            data = json.load(file)

        for item in data:
            contact = item.pop('contact',None)
            role = item.pop('role',None)
            

            if contact:
                errors = SimpleContactSchema().validate(contact)
                if errors:
                    return errors, 422
            
            if role:
                errors = SimpleRoleSchema().validate(role)
                if errors:
                    return errors, 422
                
            errors  = UserGetSchemaJSON().validate(item)
            if errors:
                    return errors, 422
            
            item['contact'] = contact
            item['role'] = role
                



        return jsonify(data),200

    @blp_json.arguments(UserPostSchemaJSON)
    @blp_json.response(201, UserPostSchemaJSON)
    def post(self, payload):

        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            abort(422)
        

        reversed_payload_gen = (item for item in reversed(data))
        ordered_payload = {'id': next(reversed_payload_gen)['id']+1}
        ordered_payload.update(payload)

        data.append(ordered_payload)

        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

       
        

        
        return jsonify(payload),201
