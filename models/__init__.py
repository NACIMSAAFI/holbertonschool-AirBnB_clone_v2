#!/usr/bin/python3
"""
the models package
"""
from os import getenv
storage_t = getenv("HBNB_TYPE_STORAGE")
if storage_t == "db": 
    from models.engine.file_storage import FileStorage
    storage = DBStorage()
else:  
    from models.engine.db_storage import DBStorage
    storage = FileStorage()
storage.reload()
