#!/usr/bin/python3
"""
testing class Place
"""

import unittest
from models import place
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class place """

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = Place()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(place.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(Place.__doc__)

    def test_create(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, Place)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(self.my_model.name, "")
        self.assertEqual(self.my_model.city_id, "")
        self.assertEqual(self.my_model.user_id, "")
        self.assertEqual(self.my_model.description, "")
        self.assertEqual(self.my_model.number_rooms, 0)
        self.assertEqual(self.my_model.number_bathrooms, 0)
        self.assertEqual(self.my_model.max_guest, 0)
        self.assertEqual(self.my_model.price_by_night, 0)
        self.assertEqual(self.my_model.latitude, 0.0)
        self.assertEqual(self.my_model.longitude, 0.0)
        self.assertEqual(self.my_model.amenity_ids, [])

    def test_class(self):
        """ test class """
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
