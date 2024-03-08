#!/usr/bin/python3
""" Creating: BaseModel class """
import sys
import uuid
from datetime import datetime


sys.path.append('.')


class BaseModel:
    """ BaseModel class core """

    def __init__(self, *args, **kwargs):
        """ Init BaseModel instance """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        _str_ is a string representation
        Return:
            string representation of BaseModel
        """
        cls = self.__class__.__name__
        formatter = "[{}] ({}) {}"
        return (formatter.format(cls, self.id, self.__dict__))

    def save(self):
        """
        Updates public attr updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return:
            a dict containing keys/vals of _dict_ of the instance
        """
        objDict = self.__dict__.copy()
        objDict["__class__"] = self.__class__.__name__
        objDict["created_at"] = self.created_at.isoformat()
        objDict["updated_at"] = self.updated_at.isoformat()
        return (objDict)
