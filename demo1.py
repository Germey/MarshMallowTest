class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

data = [{
    'name': 'Germey',
    'age': 23
}, {
    'name': 'Mike',
    'age': 20
}]
import json
print(json.dumps(data, ensure_ascii=False))