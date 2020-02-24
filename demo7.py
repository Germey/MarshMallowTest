from marshmallow import Schema, fields, ValidationError


def validate_quantity(n):
    if n < 0:
        raise ValidationError('Quantity must be greater than 0.')
    if n > 30:
        raise ValidationError('Quantity must not be greater than 30.')


class ItemSchema(Schema):
    quantity = fields.Integer(validate=validate_quantity)


in_data = {'quantity': 31}
try:
    result = ItemSchema().load(in_data)
except ValidationError as err:
    print(err.messages)
