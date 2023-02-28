#!/usr/bin/python3
"""
testing class Amenity
"""

import unittest
from models import amenity
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class Amenity"""

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = Amenity()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(amenity.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_create(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(self.my_model.name, "")

    def test_class(self):
        """ test class """
        self.assertEqual(Amenity.name, "")
