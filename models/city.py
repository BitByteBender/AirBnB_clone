#!/usr/bin/python3
""" Creating: City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class core inherits from BaseModel """
    state_id = ""
    name = ""
