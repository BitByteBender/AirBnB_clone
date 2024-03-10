#!/usr/bin/python3
""" Unittesting Place class """
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test cases for Place class """
    def testing_attrs(self):
        """ Testing if Place class its attrs """
        plc = Place()
        self.assertTrue(hasattr(plc, "city_id"))
        self.assertTrue(hasattr(plc, "user_id"))
        self.assertTrue(hasattr(plc, "name"))
        self.assertTrue(hasattr(plc, "description"))
        self.assertTrue(hasattr(plc, "number_rooms"))
        self.assertTrue(hasattr(plc, "number_bathrooms"))
        self.assertTrue(hasattr(plc, "max_guest"))
        self.assertTrue(hasattr(plc, "price_by_night"))
        self.assertTrue(hasattr(plc, "latitude"))
        self.assertTrue(hasattr(plc, "longitude"))
        self.assertTrue(hasattr(plc, "amenity_ids"))

    def testing_attr_vals(self):
        """ Testing inits attr values"""
        plc = Place()
        self.assertEqual(plc.city_id, "")
        self.assertEqual(plc.user_id, "")
        self.assertEqual(plc.name, "")
        self.assertEqual(plc.description, "")
        self.assertEqual(plc.number_rooms, 0)
        self.assertEqual(plc.number_bathrooms, 0)
        self.assertEqual(plc.max_guest, 0)
        self.assertEqual(plc.price_by_night, 0)
        self.assertEqual(plc.latitude, 0.0)
        self.assertEqual(plc.longitude, 0.0)
        self.assertEqual(plc.amenity_ids, [])

    def testing_attrs(self):
        """ Testing attrs params """
        plc = Place()
        plc.city_id = "999"
        plc.user_id = "101"
        plc.name = "Half Life Penthouse"
        plc.description = "Penthouse with an excellent view"
        plc.number_rooms = 15
        plc.number_bathrooms = 4
        plc.max_guest = 8
        plc.price_by_night = 987
        plc.latitude = 150.9154
        plc.longitude = -425.1543
        plc.amenity_ids = ['5', '7', '8']
        self.assertEqual(plc.city_id, "999")
        self.assertEqual(plc.user_id, "101")
        self.assertEqual(plc.name, "Half Life Penthouse")
        self.assertEqual(plc.description, "Penthouse with an excellent view")
        self.assertEqual(plc.number_rooms, 15)
        self.assertEqual(plc.number_bathrooms, 4)
        self.assertEqual(plc.max_guest, 8)
        self.assertEqual(plc.price_by_night, 987)
        self.assertEqual(plc.latitude, 150.9154)
        self.assertEqual(plc.longitude, -425.1543)
        self.assertEqual(plc.amenity_ids, ['5', '7', '8'])

    def testing_to_dict_method(self):
        """ Testing the to_dict() method """
        plc = Place()
        plc.city_id = "845"
        plc.user_id = "8954"
        plc.name = "Two-story House"
        plcDict = plc.to_dict()
        self.assertIsInstance(plcDict, dict)
        self.assertEqual(plcDict["__class__"], "Place")
        self.assertEqual(plcDict["city_id"], "845")
        self.assertEqual(plcDict["user_id"], "8954")
        self.assertEqual(plcDict["name"], "Two-story House")

    def test_BM_inheritance(self):
        """ Testing inheritance from BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))


if (__name__ == "__main__"):
    unittest.main()
