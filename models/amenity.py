#!/usr/bin/python3

"""Amenity Module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing class Amenity
        """
        BaseModel.__init__(self, *args, **kwargs)
