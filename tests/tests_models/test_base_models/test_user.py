#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestCity(unittest.TestCase):
    """tests for the class User"""
    def setUp(self):
        self.user = User()

    def testAttributesPresent(self):
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
