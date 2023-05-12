#!/usr/bin/python3

"""
Test Cases for the review Module
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Review Cases
    """
    def setUp(self):
        """
        Set up test objects
        """
        self.review1 = Review()
        self.review2 = Review()

        self.review1.place_id = "49faff9a-6318-451f-87b6-910505c55907"
        self.review1.user_id = "af9b4cbd-2ce1-4e6e-8259-f578097dd15f"
        self.review1.text = "I enjoyed staying there"

    def tearDown(self):
        """
        Tear Down Objects
        """
        pass

    def test_review_id_type(self):
        """
        Checks for the type of review id
        """
        self.assertTrue(type(self.review1.id), str)

    def test_review_id_unique(self):
        """
        Checks if each id is unique
        """
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_review_instance(self):
        """
        Checks for the the instance user object
        """
        self.assertTrue(isinstance(self.review1, Review))

    def test_review_inheritance(self):
        """
        Checks that review inherits from the BaseModel
        """
        self.assertTrue(issubclass(self.review2.__class__, BaseModel))

    def test_review_attributes_type(self):
        """
        Checks the type of review attributes
        """
        self.assertTrue(type(self.review1.place_id), str)
        self.assertTrue(type(self.review1.user_id), str)
        self.assertTrue(type(self.review1.text), str)

    def test_review_attributes_in_dict(self):
        """
        Checks that each attribute of the objects is present in
        the objects dictionary
        """
        obj1_dict = self.review1.__dict__
        obj2_dict = self.review2.__dict__

        self.assertIn("place_id", obj1_dict)
        self.assertIn("user_id", obj1_dict)
        self.assertIn("text", obj1_dict)
        self.assertIn("id", obj1_dict)
        self.assertIn("updated_at", obj2_dict)
        self.assertIn("created_at", obj2_dict)

    def test_review_obj_save(self):
        """
        Test for save()
        """
        self.review1.save()
        self.assertLess(self.review1.created_at, self.review1.updated_at)

    def test_review_obj_to_dict(self):
        """
        Test for to_dict()
        """
        self.review2_dict = self.review2.to_dict()

        self.assertTrue(type(self.review2_dict["__class__"]) == str)
        self.assertTrue(type(self.review2_dict["created_at"]) == str)
        self.assertTrue(type(self.review2_dict["updated_at"]) == str)
