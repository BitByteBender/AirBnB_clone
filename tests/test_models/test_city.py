#!/usr/bin/python3
""" Unittests from city class """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Testing usecases for City class """

    def testing_attrs(self):
        """ Testing all required attributes """
        c = City()
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(hasattr(c, 'name'))

    def test_attr_vals(self):
        """ Testing values of attributes """
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

    def testing_attrs_params(self):
        """ Testing all attrs params """
        c = City()
        c.state_id = "3094"
        c.name = "Bit City"
        self.assertEqual(c.state_id, "3094")
        self.assertEqual(c.name, "Bit City")

    def testing_to_dict_method(self):
        """ Testing the to_dict() method """
        c = City()
        c.state_id = "84235"
        c.name = "Bender City"
        cDict = c.to_dict()
        self.assertIsInstance(cDict, dict)
        self.assertEqual(cDict['__class__'], 'City')
        self.assertEqual(cDict['state_id'], "84235")
        self.assertEqual(cDict['name'], "Bender City")

    def test_BM_inheritance(self):
        """ Testing the inheritance from BaseModel class """
        self.assertTrue(issubclass(City, BaseModel))


if (__name__ == '__main__'):
    unittest.main()
