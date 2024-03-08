import json
from flask import jsonify, make_response
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import ContactCreateSchema, RoleCreateSchema



blp_json_child = Blueprint('contact, role',__name__, url_prefix='/contact', description="Create Contact and Role For JSON User")

@blp_json_child.route("/<string:uid>/contact")
class UserContactCreate(MethodView):

    @blp_json_child.arguments(ContactCreateSchema)
    @blp_json_child.response(201,ContactCreateSchema)
    def post(self, payload , uid):
        
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        

        current_data_gen = (item for item in data)

        # for else loop for checking existence of entry
        for index,entry in enumerate(current_data_gen):
            if entry['id'] == int(uid):
                if not data[index]['contact']:
                    data[index].pop('contact')
                    role = data[index].pop('role')
                    ordered_payload = {}
                    ordered_payload.update(data[index])
                    ordered_contact = {'id':uid}
                    ordered_contact.update(payload)
                    ordered_payload.update({'contact': ordered_contact})
                    ordered_payload.update({'role':role})
                    
                    data[index] = ordered_payload
                    with open('sample.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    break

                else:
                    return make_response(jsonify({'message': 'contact already there'}), 422)
                
        
        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)
        
        return payload
    

@blp_json_child.route("/<string:uid>/role")
class UserRoleCreate(MethodView):

    @blp_json_child.arguments(RoleCreateSchema)
    @blp_json_child.response(201,RoleCreateSchema)
    def post(self, payload , uid):
        
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        

        current_data_gen = (item for item in data)

        # for else loop for checking existence of entry
        for index,entry in enumerate(current_data_gen):
            if entry['id'] == int(uid):
                if not data[index]['role']:

                    data_gen = (item['role']['id'] for item in data if item['role'] is not None ) 
                    
                    

                    # extracting the last element's index and adding 1 to replicate database type indexing
                    latest_index_id = max(data_gen) + 1

                    data[index].pop('role')
                    contact = data[index].pop('contact')
                    ordered_payload = {}
                    ordered_payload.update(data[index])
                    

                    ordered_role = {'id':latest_index_id}
                    ordered_role.update(payload)

                    ordered_payload.update({'contact': contact})
                    ordered_payload.update({'role':ordered_role})
                    

                    
                    data[index] = ordered_payload
                    with open('sample.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    break

                else:
                    return make_response(jsonify({'message': 'contact already there'}), 422)
                
        
        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)
        
        return payload