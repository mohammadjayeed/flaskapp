import json
from flask import request, jsonify, make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SimpleContactSchema, SimpleRoleSchema, UserPostSchemaJSON, UserGetUpdateSchemaJSON 
from models import User

blp_json = Blueprint("json_users",__name__, description="CRUD Users")

@blp_json.route("/users/json")
class UserListCreate(MethodView):
    
    @blp_json.response(200)
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
                
            errors  = UserGetUpdateSchemaJSON().validate(item)
            if errors:
                    return errors, 422
            
            item['contact'] = contact
            item['role'] = role
                



        return data

    @blp_json.arguments(UserPostSchemaJSON)
    @blp_json.response(201, UserPostSchemaJSON)
    def post(self, payload):

        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            abort(422)
        
        # using generator for efficiency 
        reversed_data_gen = (item for item in reversed(data)) 

        last_index_id =next(reversed_data_gen)['id'] 

        # extracting the last element's index and adding 1 to replicate database type indexing
        latest_index_id = last_index_id + 1   

        # Correcting Order
        ordered_payload = {'id': latest_index_id } 

        # Appending json body with id at the top
        ordered_payload.update(payload)

        data.append(ordered_payload)

        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

        return payload

@blp_json.route("/users/json/<string:uid>")
class UserRetrieveUpdateDelete(MethodView):
    
    @blp_json.response(200)
    def get(self, uid):
        retrieved_data = {}
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        
        current_data_gen = (item for item in data)
        
        # for else loop for checking existence of entry
        for index,entry in enumerate(current_data_gen):
            if entry['id'] == int(uid):
                retrieved_data = data[index]
                contact = retrieved_data.pop('contact',None)
                role = retrieved_data.pop('role',None)
            

                if contact:
                    errors = SimpleContactSchema().validate(contact)
                    if errors:
                        return errors, 422
                
                if role:
                    errors = SimpleRoleSchema().validate(role)
                    if errors:
                        return errors, 422
                    
                errors  = UserGetUpdateSchemaJSON().validate(retrieved_data)
                if errors:
                        return errors, 422
            
                retrieved_data['contact'] = contact
                retrieved_data['role'] = role
                break

        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)

        return retrieved_data
       


    @blp_json.arguments(UserGetUpdateSchemaJSON)
    @blp_json.response(200,UserGetUpdateSchemaJSON)
    def put(self, payload, uid):
        
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        
        current_data_gen = (item for item in data)
        
        # for else loop for checking existence of entry
        for entry in current_data_gen:
            if entry['id'] == int(uid):
                entry.update(payload)
                break

        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)
                  


        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

        return payload
    
    
    def delete(self, uid):
        
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        
        current_data_gen = (item for item in data)

        # for else loop for checking existence of entry
        for index,entry in enumerate(current_data_gen):
            if entry['id'] == int(uid):
                data.pop(index)
                break
        
        else:
            abort(404, 'No such entry exists')


        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

        return {"message":"Entry Deleted."}