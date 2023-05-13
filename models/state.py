#!/usr/bin/python3

"""
State Module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing class State
        """
        BaseModel.__init__(self, *args, **kwargs)
