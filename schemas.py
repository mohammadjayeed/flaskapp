from marshmallow import Schema, fields


class SimpleContactSchema(Schema):
    id = fields.Int()
    phone = fields.Str()
    address = fields.Str()
    city = fields.Str()
    country = fields.Str()

class SimpleRoleSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class UserSchema(Schema):
    
    id = fields.Int()
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    active = fields.Bool()
    company = fields.Str(required=True)
    sex = fields.Str(validate=lambda x: x in ['M', 'F'], required=True)
    contact = fields.Nested(SimpleContactSchema)
    role = fields.Nested(SimpleRoleSchema)

class UserPostSchemaJSON(Schema):
    
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    active = fields.Bool(required=True)
    company = fields.Str(required=True)
    sex = fields.Str(validate=lambda x: x in ['M', 'F'], required=True)

class UserGetUpdateSchemaJSON(Schema):
    
    id = fields.Int(required=False)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    active = fields.Bool(required=True)
    company = fields.Str(required=True)
    sex = fields.Str(validate=lambda x: x in ['M', 'F'], required=True)

