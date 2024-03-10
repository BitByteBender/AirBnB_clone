#!/usr/bin/python3
""" Unittesting State class """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test cases from State class """
    def testing_attrs(self):
        """ Testing if State class has an attr called "name" """
        st = State()
        self.assertTrue(hasattr(st, "name"))

    def testing_attr_vals(self):
        """ Testing dflt value of "name" attr """
        st = State()
        self.assertEqual(st.name, "")

    def testing_attrs__params(self):
        """ Testing attr "name" params """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def testing_to_dict_method(self):
        """ Testing the to_dict method """
        st = State()
        st.name = "Bouznika"
        stDict = st.to_dict()
        self.assertIsInstance(stDict, dict)
        self.assertEqual(stDict["__class__"], "State")
        self.assertEqual(stDict["name"], "Bouznika")

    def testing_BM_inheritance(self):
        """ Testing inheritance from BaseModel """
        self.assertTrue(issubclass(State, BaseModel))


if (__name__ == "__main__"):
    unittest.main()
