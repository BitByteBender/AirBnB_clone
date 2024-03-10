#!/usr/bin/python3
""" Unittesting Amenity class """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def testing_attrs(self):
        amt = Amenity()
        self.assertTrue(hasattr(amt, "name"))

    def testing_attr_vals(self):
        amt = Amenity()
        self.assertEqual(amt.name, "")

    def testing_attrs_params(self):
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def testing_to_dict_method(self):
        amt = Amenity()
        amt.name = "AC"
        amtDict = amt.to_dict()
        self.assertIsInstance(amtDict, dict)
        self.assertEqual(amtDict["__class__"], "Amenity")
        self.assertEqual(amtDict["name"], "AC")

    def testing_BM_inheritance(self):
        self.assertTrue(issubclass(Amenity, BaseModel))


if (__name__ == "__main__"):
    unittest.main()
