#!/usr/bin/python3
""" Creating: Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review core class that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
