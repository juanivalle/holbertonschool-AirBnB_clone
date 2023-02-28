#!/usr/bin/python3
"""
testing class State
"""

import unittest
from models import state
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class """

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = State()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(state.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(State.__doc__)

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(self.my_model.name, "")

    def test_create(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_class(self):
        """ test class """
        self.assertEqual(State.name, "")
