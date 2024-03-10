#!/usr/bin/python3
"""Unittests for FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Unittesting core functionality of FileStorage """
    def setUp(self):
        self.storage = FileStorage()

    def testing_all_method(self):
        o1 = BaseModel()
        o2 = BaseModel()
        self.storage.new(o1)
        self.storage.new(o2)
        objs = self.storage.all()
        self.assertEqual(len(objs), 2)
        self.assertIn(o1, objs.values())
        self.assertIn(o2, objs.values())

    def testing_new_method(self):
        o = BaseModel()
        self.storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertIn(key, self.storage.all())

    def testing_save_method(self):
        o = BaseModel()
        self.storage.new(o)
        self.storage.save()
        with open("file.json", mode='r', encoding="utf-8") as file:
            dt = json.load(file)
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertIn(key, dt)

    def testing_reload_method(self):
        o = BaseModel()
        self.storage.new(o)
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertIn(key, objs)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def testing_inheritance(self):
        self.assertTrue(self.storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
