#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """for the class City"""

    def setUp(self):
        """set up method"""
        self.self  = City()

    def testAttributesPresent(self):
        """attrs are present"""
        self.assertTrue(hasattr(self.self, 'state_id'))
        self.assertTrue(hasattr(self.self, 'name'))

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.self, BaseModel)
