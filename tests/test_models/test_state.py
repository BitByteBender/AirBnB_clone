#!/usr/bin/python3
""" Unittesting State class """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def testing_attrs(self):
        st = State()
        self.assertTrue(hasattr(st, "name"))

    def testing_attr_vals(self):
        st = State()
        self.assertEqual(st.name, "")

    def testing_attrs__params(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def testing_to_dict_method(self):
        st = State()
        st.name = "Bouznika"
        stDict = st.to_dict()
        self.assertIsInstance(stDict, dict)
        self.assertEqual(stDict["__class__"], "State")
        self.assertEqual(stDict["name"], "Bouznika")

    def testing_BM_inheritance(self):
        self.assertTrue(issubclass(State, BaseModel))


if (__name__ == "__main__"):
    unittest.main()
