#!/usr/bin/python3

"""
Test Cases for the state Module
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    State Cases
    """
    def setUp(self):
        """
        Set up test objects
        """
        self.state1 = State()
        self.state2 = State()

        self.state1.name = "Lagos"

    def tearDown(self):
        """
        Tear Down Objects
        """
        pass

    def test_state_id_type(self):
        """
        Checks for object type
        """
        self.assertTrue(type(self.state1.id), str)

    def test_state_id_unique(self):
        """
        Checks if each id is unique
        """
        self.assertNotEqual(self.state1.id, self.state2.id)

    def test_state_instance(self):
        """
        Checks the object's instance
        """
        self.assertTrue(isinstance(self.state1, State))

    def test_state_inheritance(self):
        """
        Checks that State inherits from the BaseModel
        """
        self.assertTrue(issubclass(self.state2.__class__, BaseModel))

    def test_state_attributes_type(self):
        """
        Checks the type of state attributes
        """
        self.assertTrue(type(self.state1.name), str)

    def test_state_attributes_in_dict(self):
        """
        Checks that each attribute of the objects is present in
        the objects dictionary
        """
        obj1_dict = self.state1.__dict__
        obj2_dict = self.state2.__dict__

        self.assertIn("name", obj1_dict)
        self.assertIn("id", obj1_dict)
        self.assertIn("updated_at", obj2_dict)
        self.assertIn("created_at", obj2_dict)

    def test_state_obj_save(self):
        """
        Test for save()
        """
        self.state1.save()
        self.assertLess(self.state1.created_at, self.state1.updated_at)

    def test_state_obj_to_dict(self):
        """
        Test for to_dict()
        """
        self.state2_dict = self.state2.to_dict()

        self.assertTrue(type(self.state2_dict["__class__"]) == str)
        self.assertTrue(type(self.state2_dict["created_at"]) == str)
        self.assertTrue(type(self.state2_dict["updated_at"]) == str)


if __name__ == "__main__":
    unittest.main()
