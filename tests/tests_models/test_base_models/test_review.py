#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestCity(unittest.TestCase):
    """the class Review"""

    def setUp(self):
        self.review = Review()

    def testClassPresent(self):
        """it check if class exists"""
        self.assertEqual(
                str(type(self.review)), "<class 'models.review.Review'>"
                )

    def testAttrTypes(self):
        """check for the right attr types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.user_id, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
