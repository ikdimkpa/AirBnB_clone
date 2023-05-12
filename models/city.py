#!/usr/bin/python3

"""City Module"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class City
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing class City
        """
        BaseModel.__init__(self, *args, **kwargs)
