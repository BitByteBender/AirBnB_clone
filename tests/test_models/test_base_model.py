#!/usr/bin/python3
""" Unittests for BaseModel class """
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
import datetime


class TestBaseModel_Init(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)


class TestBaseModel_Dict(unittest.TestCase):
    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if (__name__ == "__main__"):
    unittest.main()
