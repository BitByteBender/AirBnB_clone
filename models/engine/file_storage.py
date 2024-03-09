#!/usr/bin/python3
""" Creating: FileStorage Class """
import json


class FileStorage:
    """ FileStorage Class Core """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return:
            returns a dict __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in objects with key
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes objs to JSON file path: _file_path)
        """
        serializeObjs = {}
        for k, v in self.__objects.items():
            serializeObjs[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as file:
            json.dump(serializeObjs, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (_file_path) exists
        Otherwise nothing.

        If file doesn't exist throw an exception
        """
        try:
            from models.base_model import BaseModel
            from models.user import User
            with open(self.__file_path, mode='r', encoding="utf-8") as file:
                serializeObjs = json.load(file)
                for k, val in serializeObjs.items():
                    cls_name, objId = k.split('.')
                    if cls_name == 'User':
                        obj = User(**val)
                    else:
                        obj = BaseModel(**val)
                    self.__objects[k] = obj
        except FileNotFoundError:
            pass
