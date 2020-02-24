from attr import attrs, attrib
from marshmallow import Schema, fields, post_load


@attrs
class User(object):
    name = attrib()
    age = attrib()


class UserSchema(Schema):
    name = fields.Str()
    age = fields.Integer()
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


data = {
    'name': 'Germey',
    'age': 'hello'
}

from marshmallow import ValidationError


try:
    schema = UserSchema()
    user, errors = schema.load(data)
    print(user, errors)
except ValidationError as e:
    print('e.message', e.messages)
    print('e.valid_data', e.valid_data)
