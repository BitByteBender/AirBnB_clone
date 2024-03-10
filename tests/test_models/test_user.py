#!/usr/bin/python3
""" Unittests for User class """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Testing usecase for User class """

    def testing_attrs(self):
        """ Testing all required attrs for User class """
        usr = User()
        self.assertTrue(hasattr(usr, 'email'))
        self.assertTrue(hasattr(usr, 'password'))
        self.assertTrue(hasattr(usr, 'first_name'))
        self.assertTrue(hasattr(usr, 'last_name'))

    def testing_attr_vals(self):
        """ Testing dflt values of attrs """
        usr = User()
        self.assertEqual(usr.email, "")
        self.assertEqual(usr.password, "")
        self.assertEqual(usr.first_name, "")
        self.assertEqual(usr.last_name, "")

    def testing_attrs_params(self):
        """ Testing attributes params """
        usr = User()
        usr.email = "madskillz.oneofone@google.com"
        usr.password = "tester101"
        usr.first_name = "Soufiane"
        usr.last_name = "Ataafi"
        self.assertEqual(usr.email, "madskillz.oneofone@google.com")
        self.assertEqual(usr.password, "tester101")
        self.assertEqual(usr.first_name, "Soufiane")
        self.assertEqual(usr.last_name, "Ataafi")

    def testing_to_dict_method(self):
        """ Testing the to_dict() method """
        usr = User()
        usr.email = "madskillz.oneofone@google.com"
        usr.password = "notgonnalikeit123"
        usr.first_name = "Souf"
        usr.last_name = "Cleve"
        usrDict = usr.to_dict()
        self.assertIsInstance(usrDict, dict)
        self.assertEqual(usrDict['__class__'], 'User')
        self.assertEqual(usrDict['email'], "madskillz.oneofone@google.com")
        self.assertEqual(usrDict['password'], "notgonnalikeit123")
        self.assertEqual(usrDict['first_name'], "Souf")
        self.assertEqual(usrDict['last_name'], "Cleve")

    def testing_BM_inheritance(self):
        """ Testing the inheritance from BaseModel class """
        self.assertTrue(issubclass(User, BaseModel))


if (__name__ == "__main__"):
    unittest.main()
