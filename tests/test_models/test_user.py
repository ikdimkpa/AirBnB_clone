#!/usr/bin/python3

"""
Test Cases for the user Module
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    User Cases
    """
    def setUp(self):
        """
        Set up test objects
        """
        self.user1 = User()
        self.user2 = User()

        self.user1.email = "folua@gmail.com"
        self.user1.password = "qwert1324"
        self.user1.first_name = "Ade"
        self.user1.last_name = "Sama"

        self.user2.email = "smart@mail.com"
        self.user2.password = "qwgavby4"
        self.user2.first_name = "Smart"
        self.user2.last_name = "Joke"

    def tearDown(self):
        """
        Tear Down Objects
        """
        pass

    def test_user_id_type(self):
        """
        Checks for the type of user's id
        """
        self.assertTrue(type(self.user1.id), str)

    def test_user_id_unique(self):
        """
        Checks if each id is unique
        """
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_user_instance(self):
        """
        Checks for the the instance user object
        """
        self.assertTrue(isinstance(self.user1, User))

    def test_user_inheritance(self):
        """
        Checks that User inherits from the BaseModel
        """
        self.assertTrue(issubclass(self.user2.__class__, BaseModel))

    def test_user_attributes_type(self):
        """
        Checks the type of user attributes
        """
        self.assertTrue(type(self.user1.email), str)
        self.assertTrue(type(self.user1.email), str)
        self.assertTrue(type(self.user2.email), str)
        self.assertTrue(type(self.user2.email), str)

    def test_user_attributes_in_dict(self):
        """
        Checks that each attribute of the objects is present in
        the objects dictionary
        """
        obj1_dict = self.user1.__dict__
        obj2_dict = self.user1.__dict__

        self.assertIn("email", obj1_dict)
        self.assertIn("password", obj1_dict)
        self.assertIn("first_name", obj2_dict)
        self.assertIn("last_name", obj2_dict)
        self.assertIn("id", obj1_dict)
        self.assertIn("updated_at", obj2_dict)
        self.assertIn("created_at", obj2_dict)

    def test_user_obj_save(self):
        """
        Test for save()
        """
        self.user1.save()
        self.assertLess(self.user1.created_at, self.user1.updated_at)

    def test_user_obj_to_dict(self):
        """
        Test for to_dict()
        """
        self.user2_dict = self.user2.to_dict()

        self.assertTrue(type(self.user2_dict["__class__"]) == str)
        self.assertTrue(type(self.user2_dict["created_at"]) == str)
        self.assertTrue(type(self.user2_dict["updated_at"]) == str)
