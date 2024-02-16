from uuid import uuid4
from db import DBStorage
from datetime import datetime

db = DBStorage()

class ManagedDB:

    _created_at = datetime.utcnow().isoformat()

    def __init__(self, created_at=None) -> None:
        self.created_at = created_at

    @property
    def created_at(self):
        return datetime.fromisoformat(self._created_at)
    
    @created_at.setter
    def created_at(self, value):
        if isinstance(value, str):
            self._created_at = value
        elif isinstance(value, datetime):
            self._created_at = value.isoformat()

    @classmethod
    def get(cls, id):
        data = db.get(cls=cls, id=id)
        return cls(**data)

    @classmethod
    def all(cls):
        return [cls(**data) for data in db.all(cls=cls)]

    def save(self):
        db.add(obj=self)
        db.save()

    @classmethod
    def match(cls, **kwargs):
        for key, value in kwargs.items():
            for obj in db.all(cls):
                if key in obj and obj.get(key) == value:
                    return cls(**obj)       

class User(ManagedDB):

    def __init__(self, name, username, password, id = None, **kwargs) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.id = id

        if self.id is None:
            self.id = str(uuid4())

        super().__init__(**kwargs)
    
    def to_dict(self):
        attrs = ['name', 'username', 'password', 'id', 'created_at']
        objs = {}
        for attr in attrs:
            objs.update({
                attr: getattr(self, attr).isoformat() if isinstance(getattr(self, attr), datetime) else getattr(self, attr)
            })
        
        return objs

class Post(ManagedDB):
    
    def __init__(self, title, body, id=None, **kwargs) -> None:
        self.title = title
        self.body = body
        self.id = id

        if self.id is None:
            self.id = str(uuid4())

        super().__init__(**kwargs)
        

    def to_dict(self):
        attrs = ['title', 'body', 'id', 'created_at']
        objs = {}
        for attr in attrs:
            objs.update({
                attr: getattr(self, attr).isoformat() if isinstance(getattr(self, attr), datetime) else getattr(self, attr)
            })
        
        return objs

class Comment(ManagedDB):

    def __init__(self, body, user, post, id=None, **kwargs) -> None:
        self.body = body
        self.user_id = user.id
        self.post_id = post.id
        self.id = id

        if self.id is None:
            self.id = str(uuid4())

        super().__init__(**kwargs)
        

    @property
    def user(self):
        return db.get(cls=User, id=self.user_id)

    @property
    def post(self):
        return db.get(cls=Post, id=self.post_id)

    def to_dict(self):
        attrs = ['body', 'user_id', 'post_id', 'id', 'created_at']
        objs = {}
        for attr in attrs:
            objs.update({
                attr: getattr(self, attr).isoformat() if isinstance(getattr(self, attr), datetime) else getattr(self, attr)
            })
        
        return objs