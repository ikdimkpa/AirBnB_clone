#!/usr/bin/python3

"""
Test Cases for the place Module
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Place Cases
    """
    def setUp(self):
        """
        Set up test objects
        """
        self.place1 = Place()
        self.place2 = Place()

        self.place1.city_id = "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4"
        self.place1.user_id = "a42ee380-c959-450e-ad29-c840a898cfce"
        self.place1.name = "Lagos"
        self.place1.description = "Affordable"
        self.place1.number_rooms = 18
        self.place1.number_bathrooms = 15
        self.place1.max_guest = 70
        self.place1.price_by_night = 10000
        self.place1.latitude = 10.2
        self.place1.longitude = 89.3
        self.place1.amenity_ids = "49faff9a-6318-451f-87b6-910505c55907"

    def tearDown(self):
        """
        Tear Down Objects
        """
        pass

    def test_place_id_type(self):
        """
        Checks for the type of place id
        """
        self.assertTrue(type(self.place2.id), str)

    def test_place_id_unique(self):
        """
        Checks if each id is unique
        """
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_place_instance(self):
        """
        Checks for the the instance place object
        """
        self.assertTrue(isinstance(self.place1, Place))

    def test_place_inheritance(self):
        """
        Checks that Place inherits from the BaseModel
        """
        self.assertTrue(issubclass(self.place2.__class__, BaseModel))

    def test_place_attributes_type(self):
        """
        Checks the type of place attributes
        """
        self.assertTrue(type(self.place1.city_id), str)
        self.assertTrue(type(self.place1.user_id), str)
        self.assertTrue(type(self.place1.name), str)
        self.assertTrue(type(self.place1.description), str)
        self.assertTrue(type(self.place1.number_rooms), int)
        self.assertTrue(type(self.place1.number_bathrooms), int)
        self.assertTrue(type(self.place1.max_guest), int)
        self.assertTrue(type(self.place1.price_by_night), int)
        self.assertTrue(type(self.place1.latitude), float)
        self.assertTrue(type(self.place1.longitude), float)
        self.assertTrue(type(self.place1.amenity_ids), str)

    def test_place_attributes_in_dict(self):
        """
        Checks that each attribute of the objects is present in
        the objects dictionary
        """
        obj1_dict = self.place1.__dict__

        self.assertIn("city_id", obj1_dict)
        self.assertIn("user_id", obj1_dict)
        self.assertIn("name", obj1_dict)
        self.assertIn("description", obj1_dict)
        self.assertIn("number_rooms", obj1_dict)
        self.assertIn("number_bathrooms", obj1_dict)
        self.assertIn("max_guest", obj1_dict)
        self.assertIn("price_by_night", obj1_dict)
        self.assertIn("latitude", obj1_dict)
        self.assertIn("longitude", obj1_dict)
        self.assertIn("amenity_ids", obj1_dict)
        self.assertIn("id", obj1_dict)
        self.assertIn("updated_at", obj1_dict)
        self.assertIn("created_at", obj1_dict)

    def test_place_obj_save(self):
        """
        Test for save()
        """
        self.place2.save()
        self.assertLess(self.place2.created_at, self.place2.updated_at)

    def test_place_obj_to_dict(self):
        """
        Test for to_dict()
        """
        self.place2_dict = self.place2.to_dict()

        self.assertTrue(type(self.place2_dict["__class__"]) == str)
        self.assertTrue(type(self.place2_dict["created_at"]) == str)
        self.assertTrue(type(self.place2_dict["updated_at"]) == str)


if __name__ == "__main__":
    unittest.main()
