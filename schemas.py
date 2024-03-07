from marshmallow import Schema, fields


class SimpleContactSchema(Schema):
    id = fields.Int(dump_only=True)
    phone = fields.Str(required=False)
    address = fields.Str(required=False)
    city = fields.Str(required=False)
    country = fields.Str(required=False)

class SimpleRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class UserSchema(Schema):
    
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    active = fields.Bool(required=False)
    company = fields.Str(required=True)
    sex = fields.Str(validate=lambda x: x in ['M', 'F'], required=True)
    contact = fields.Nested(SimpleContactSchema, required=False)
    role = fields.List(fields.Nested(SimpleRoleSchema), required=False)