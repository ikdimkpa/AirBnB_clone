#!/usr/bin/python3

"""
Module for class Place that inherits
from class BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place; full description of
       the house to be rented
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = ""
