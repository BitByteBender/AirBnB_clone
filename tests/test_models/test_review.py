#!/usr/bin/python3
""" Unittests for Review class """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Testing Review class """
    def testing_attrs(self):
        """ Testing all required attrs """
        rv = Review()
        self.assertTrue(hasattr(rv, "place_id"))
        self.assertTrue(hasattr(rv, "user_id"))
        self.assertTrue(hasattr(rv, "text"))

    def testing_attr_vals(self):
        """ Testing attr values """
        rv = Review()
        self.assertEqual(rv.place_id, "")
        self.assertEqual(rv.user_id, "")
        self.assertEqual(rv.text, "")

    def testing_attrs(self):
        """ Testing attrs params """
        rv = Review()
        rv.place_id = "895"
        rv.user_id = "1521"
        rv.text = "Wonderful place for vacation!"
        self.assertEqual(rv.place_id, "895")
        self.assertEqual(rv.user_id, "1521")
        self.assertEqual(rv.text, "Wonderful place for vacation!")

    def testing_to_dict_method(self):
        """ Testing the to_dict() method """
        rv = Review()
        rv.place_id = "995"
        rv.user_id = "3656"
        rv.text = "Dreamland isn't it!"
        rvDict = rv.to_dict()
        self.assertIsInstance(rvDict, dict)
        self.assertEqual(rvDict["__class__"], "Review")
        self.assertEqual(rvDict["place_id"], "995")
        self.assertEqual(rvDict["user_id"], "3656")
        self.assertEqual(rvDict["text"], "Dreamland isn't it!")

    def testing_BM_inheritance_from(self):
        """ Testing inheritance from BaseModel class """
        self.assertTrue(issubclass(Review, BaseModel))


if (__name__ == "__main__"):
    unittest.main()
