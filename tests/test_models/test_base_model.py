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
    """ Unittesting Base Class """
    def testing_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)


class TestBaseModel_Dict(unittest.TestCase):
    """ Unittesting to_dict() method """
    def testing_to_dict(self):
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


class TestBaseModel_Core(unittest.TestCase):
    """ Unittesting core functionality of BaseModel """
    def testing_instance_creation(self):
        md = BaseModel()
        self.assertIsInstance(md, BaseModel)

    def testing_id_generation(self):
        md1 = BaseModel()
        md2 = BaseModel()
        self.assertNotEqual(md1.id, md2.id)

    def testing_created_at(self):
        md = BaseModel()
        self.assertIsInstance(md.created_at, datetime.datetime)

    def testing_updated_at(self):
        md = BaseModel()
        self.assertIsInstance(md.updated_at, datetime.datetime)

    def testing_str_repr(self):
        md = BaseModel()
        self.assertTrue("[BaseModel]" in str(md))

    def testing_save_method(self):
        md = BaseModel()
        current_updated_at = md.updated_at
        md.save()
        self.assertNotEqual(current_updated_at, md.updated_at)


if (__name__ == "__main__"):
    unittest.main()
