#!/usr/bin/python3

"""
Unittest Cases for class BaseModel
"""

import io
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """All Test Cases"""
    def setUp(self):
        """Sets up instances"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """Tear Down instances"""

    def test_id_is_string(self):
        """
        Ensures that the id is in string format
        """
        self.assertTrue(type(self.base1.id) == str)

    def test_id_is_unique(self):
        """
        Check that each id is unique
        """
        self.assertTrue(self.base1.id != self.base2.id)

    def test_save(self):
        """
        Test for save()
        """
        self.base1.save()
        self.assertLess(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        """
        Test for to_dict()
        """
        self.base_dict = self.base1.to_dict()

        self.assertTrue(type(self.base_dict["__class__"]) == str)
        self.assertTrue(type(self.base_dict["created_at"]) == str)
        self.assertTrue(type(self.base_dict["updated_at"]) == str)

    def test_str(self):
        """
        Test for the __str__()
        """
        pass

    def test_datetime(self):
        """
        Checks that created_at and updated_at
        are datetime
        """
        self.assertTrue(type(self.base1.created_at) == datetime)
        self.assertTrue(type(self.base2.updated_at) == datetime)

    def test_obj_instance(self):
        self.assertTrue(isinstance(self.base1, BaseModel))


if __name__ == "__main__":
    unittest.main()
