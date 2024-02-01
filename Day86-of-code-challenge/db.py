import json

class DBStorage:

    __data = {}


    def __init__(self) -> None:
        self.reload()

    def reload(self):
        try:
            with open('db.json', 'r') as f:
                self.__data = json.load(f)

        except FileNotFoundError:
            self.__data = {}

    def all(self, cls):
        return [
            self.__data.get(key) for key in self.__data.keys() 
            if key.startswith(cls.__name__)
        ]
    
    def add(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__data.update({key: obj.to_dict()})

    def get(self, cls, id):
        return self.__data.get(cls.__name__ + '.' + id)

    def save(self):
        with open('db.json', 'w') as f:
            json.dump(self.__data, f)