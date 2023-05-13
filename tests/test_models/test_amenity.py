#!/usr/bin/python3

"""
Test Cases for the Amenity Module
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Amenity Cases
    """
    def setUp(self):
        """
        Set up test objects
        """
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

        self.amenity1.name = "The Place"

    def tearDown(self):
        """
        Tear Down Objects
        """
        pass

    def test_amenity_id_type(self):
        """
        Checks for object type
        """
        self.assertTrue(type(self.amenity1.id), str)

    def test_amenity_id_unique(self):
        """
        Checks if each id is unique
        """
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

    def test_amenity_instance(self):
        """
        Checks the object's instance
        """
        self.assertTrue(isinstance(self.amenity1, Amenity))

    def test_amenity_inheritance(self):
        """
        Checks that Amenity inherits from the BaseModel
        """
        self.assertTrue(issubclass(self.amenity2.__class__, BaseModel))

    def test_amenity_attributes_type(self):
        """
        Checks the type of amenity attributes
        """
        self.assertTrue(type(self.amenity1.name), str)

    def test_amenity_attributes_in_dict(self):
        """
        Checks that each attribute of the objects is present in
        the objects dictionary
        """
        obj1_dict = self.amenity1.__dict__
        obj2_dict = self.amenity2.__dict__

        self.assertIn("name", obj1_dict)
        self.assertIn("id", obj1_dict)
        self.assertIn("updated_at", obj2_dict)
        self.assertIn("created_at", obj2_dict)

    def test_amenity_obj_save(self):
        """
        Test for save()
        """
        self.amenity1.save()
        self.assertLess(self.amenity1.created_at, self.amenity1.updated_at)

    def test_amenity_obj_to_dict(self):
        """
        Test for to_dict()
        """
        self.amenity2_dict = self.amenity2.to_dict()

        self.assertTrue(type(self.amenity2_dict["__class__"]) == str)
        self.assertTrue(type(self.amenity2_dict["created_at"]) == str)
        self.assertTrue(type(self.amenity2_dict["updated_at"]) == str)


if __name__ == "__main__":
    unittest.main()
