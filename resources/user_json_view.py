import json
from flask import request, jsonify, make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SimpleContactSchema, SimpleRoleSchema, UserPostUpdateSchemaJSON,  UserGetSchemaJSON
from flask_jwt_extended import jwt_required

blp = Blueprint("json_users",__name__, description="CRUD Users")


@blp.route("/users/json")
class UserListCreate(MethodView):
    
    @jwt_required()
    @blp.response(200)
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
                
            errors  =  UserGetSchemaJSON().validate(item)
            if errors:
                    return errors, 422
            
            item['contact'] = contact
            item['role'] = role
                



        return data

    @jwt_required()
    @blp.arguments( UserPostUpdateSchemaJSON)
    @blp.response(201,  UserPostUpdateSchemaJSON)
    def post(self, payload):

        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        
        # using generator for efficiency 
        reversed_data_gen = (item for item in reversed(data)) 

        last_index_id =next(reversed_data_gen)['id'] 

        # extracting the last element's index and adding 1 to replicate database type indexing
        latest_index_id = last_index_id + 1   

        # Correcting Order
        ordered_payload = {'id': latest_index_id } 

        # Appending json body with id at the top
        ordered_payload.update(payload)

        # Setting Contact and Role to be None so that they can be created later inside the json file
        ordered_payload.setdefault('contact', None)
        ordered_payload.setdefault('role', None)

        data.append(ordered_payload)

        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

        return payload

@blp.route("/users/json/<int:uid>")
class UserRetrieveUpdateDelete(MethodView):

    @jwt_required()
    @blp.response(200)
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
            if entry['id'] == uid:
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
                    
                errors  =  UserGetSchemaJSON().validate(retrieved_data)
                if errors:
                        return errors, 422
            
                retrieved_data['contact'] = contact
                retrieved_data['role'] = role
                break

        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)

        return retrieved_data
       

    @jwt_required()
    @blp.arguments(UserPostUpdateSchemaJSON)
    @blp.response(200,UserPostUpdateSchemaJSON)
    def put(self, payload, uid):
        
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        
        current_data_gen = (item for item in data)
        
        # for else loop for checking existence of entry
        for entry in current_data_gen:
            if entry['id'] == uid:
                entry.update(payload)
                break

        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)
                  


        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

        return payload
    
    @jwt_required()
    def delete(self, uid):
        
        try:
            with open('sample.json', 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError:
            return make_response(jsonify({'message': 'Invalid JSON'}), 422)
        
        current_data_gen = (item for item in data)

        # for else loop for checking existence of entry
        for index,entry in enumerate(current_data_gen):
            if entry['id'] == uid:
                data.pop(index)
                break
        
        else:
            return make_response(jsonify({'message': 'No such entry exists'}), 404)


        with open('sample.json', 'w') as file:
            json.dump(data, file, indent=4)

        return {"message":"Entry Deleted."}
    

