#!/usr/bin/python3
"""
testing class Review
"""

import unittest
from models import review
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class Review"""

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = Review()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(review.__doc__)
    
    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(self.my_model.user_id, "")
        self.assertEqual(self.my_model.place_id, "")
        self.assertEqual(self.my_model.text, "")

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(Review.__doc__)

    def test_create(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_class(self):
        """ test class """
        self.assertEqual(Review.text, "")
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")

