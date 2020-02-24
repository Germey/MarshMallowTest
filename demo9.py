from pprint import pprint

from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={'required': 'Age is required.'})
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}},
    )
    email = fields.Email()


try:
    result = UserSchema().load({'email': 'foo@bar.com'})
except ValidationError as err:
    pprint(err.messages)
