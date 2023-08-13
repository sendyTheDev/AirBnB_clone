#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestCity(unittest.TestCase):
    """the class Place"""
    def setUp(self):
        self.place = Place()

    def testAttributesPresent(self):
        """the attrs are present"""
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)
