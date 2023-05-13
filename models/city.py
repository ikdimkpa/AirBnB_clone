#!/usr/bin/python3

"""
Module for class Place that inherits
from class BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class City; returns the location of the
    house to be rented
    """
    state_id = ""
    name = ""

