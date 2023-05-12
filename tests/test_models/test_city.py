#!/usr/bin/python3

"""
Test Cases for the city Module
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    City Cases
    """
    def setUp(self):
        """
        Set up test objects
        """
        self.city1 = City()
        self.city2 = City()

        self.city1.name = "Tokyo"
        self.city1.state_id = "af9b4cbd-2ce1-4e6e-8259-f578097dd15f"

    def tearDown(self):
        """
        Tear Down Objects
        """
        pass

    def test_city_id_type(self):
        """
        Checks for object type
        """
        self.assertTrue(type(self.city1.id), str)

    def test_city_id_unique(self):
        """
        Checks if each id is unique
        """
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_city_instance(self):
        """
        Checks the object's instance
        """
        self.assertTrue(isinstance(self.city1, City))

    def test_city_inheritance(self):
        """
        Checks that city inherits from the BaseModel
        """
        self.assertTrue(issubclass(self.city2.__class__, BaseModel))

    def test_city_attributes_type(self):
        """
        Checks the type of city attributes
        """
        self.assertTrue(type(self.city1.name), str)
        self.assertTrue(type(self.city1.state_id), str)

    def test_city_attributes_in_dict(self):
        """
        Checks that each attribute of the objects is present in
        the objects dictionary
        """
        obj1_dict = self.city1.__dict__
        obj2_dict = self.city2.__dict__

        self.assertIn("name", obj1_dict)
        self.assertIn("state_id", obj1_dict)
        self.assertIn("id", obj1_dict)
        self.assertIn("updated_at", obj2_dict)
        self.assertIn("created_at", obj2_dict)

    def test_city_obj_save(self):
        """
        Test for save()
        """
        self.city1.save()
        self.assertLess(self.city1.created_at, self.city1.updated_at)

    def test_city_obj_to_dict(self):
        """
        Test for to_dict()
        """
        self.city2_dict = self.city2.to_dict()

        self.assertTrue(type(self.city2_dict["__class__"]) == str)
        self.assertTrue(type(self.city2_dict["created_at"]) == str)
        self.assertTrue(type(self.city2_dict["updated_at"]) == str)
