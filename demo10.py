from marshmallow import Schema, fields
import datetime as dt
import uuid


class UserSchema(Schema):
    id = fields.UUID(missing=uuid.uuid1)
    birthdate = fields.DateTime(default=dt.datetime(2017, 9, 29))


print(UserSchema().load({}))
print(UserSchema().dump({}))
