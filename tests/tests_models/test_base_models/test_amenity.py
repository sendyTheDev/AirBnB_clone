#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestCity(unittest.TestCase):
    """class Amenity"""
    def setUp(self):
        self.amenity = Amenity()

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def testAttrTypes(self):
        """right attr types"""
        self.assertIsInstance(self.amenity.name, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)
