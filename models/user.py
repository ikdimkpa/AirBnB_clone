#!/usr/bin/python3

"""
Module for class Place that inherits
from class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class for user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
