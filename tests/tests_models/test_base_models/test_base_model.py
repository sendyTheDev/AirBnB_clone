#!/usr/bin/python3
"""unittests for base_model.py"""
import unittest
from models.base_model import BaseModel

class TestBaseModelInstatioation(unittest.TestCase):
    """Tests for BaseModel class instantiation"""
    def test_instance_id_is_unique(self):
        ModelA = BaseModel()
        ModelB = BaseModel()

        self.assertNotEqual(ModelA.id, ModelB.id)

    def test_instance_creation_from_dict_repsentation(self):
        ModelA = BaseModel()
        ModelB = BaseModel(**ModelA.to_dict())

        self.assertEqual(ModelA.id, ModelB.id)
