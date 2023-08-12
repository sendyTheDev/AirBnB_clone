#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class instantiation
    """

    def test_instance_id_is_unique(self):
        self.modelA = BaseModel()
        self.modelB = BaseModel()

        self.assertNotEqual(self.modelA.id, self.modelB.id)

    def test_instance_creation_from_dict_repsentation(self):
        self.modelA = BaseModel()
        self.modelB = BaseModel(**self.modelA.to_dict())

        self.assertEqual(self.modelA.id, self.modelB.id)


if __name__ == "__main__":
    unittest.main()
