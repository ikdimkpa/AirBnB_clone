#!/usr/bin/python3

"""
User Module
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

    def __init__(self, *args, **kwargs):
        """
        Initializing the User Class
        """
        BaseModel.__init__(self, *args, **kwargs)
