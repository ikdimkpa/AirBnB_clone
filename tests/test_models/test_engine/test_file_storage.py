#!/usr/bin/python3

"""
Test cases for objects storage
"""
import os
import unittest
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    class FileStorage
    """
    def setUp(self):
        """
        Set Up
        """
        try:
            remove("file.json")
        except Exception:
            pass

    def tearDown(self):
        """
        Tear Down
        """
        pass
