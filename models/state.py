#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from os import getenv
import models
from models.city import City

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """returns the list of City instances"""
            instance_list = []
            for i in models.storage.all(City).values():
                if i.state_id == self.id:
                    instance_list.append(i)
            return instance_list
