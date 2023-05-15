#!/usr/bin/python3

"""
init module for the models; initializes the models
directory to become a package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
print("")
