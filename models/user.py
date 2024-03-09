#!/usr/bin/python3
""" Creating: User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Core User class that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
