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
    'age': 23
}

schema = UserSchema()
user = schema.load(data)
print(user)

result = schema.dump(user)
print('result', result)