#!/usr/bin/python3

"""
Module for class Place that inherits
from class BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""

    place_id = ""
    user_id = ""
    text = ""

