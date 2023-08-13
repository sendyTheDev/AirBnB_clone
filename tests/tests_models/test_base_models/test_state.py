#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestCity(unittest.TestCase):
    """tests for the class State"""

    def setUp(self):
        self.state = State()

    def testClassPresent(self):
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.state, 'name'))

    def testAttrTypes(self):
        self.assertIsInstance(self.state.name, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
