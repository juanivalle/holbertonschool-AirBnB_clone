#!/usr/bin/python3
"""
testing class City
"""

import unittest
from models import city
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class City """

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = City()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(city.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(City.__doc__)

    def test_create(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(self.my_model.name, "")
        self.assertEqual(self.my_model.state_id, "")

    def test_class(self):
        """ test class """
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
