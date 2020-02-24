from attr import attrs, attrib
from cattr import structure, unstructure

@attrs
class User(object):
    name = attrib()
    age = attrib()

data = {
    'name': 'Germey',
    'age': 23
}
user = structure(data, User)
print('user', user)
json = unstructure(user)
print('json', json)
