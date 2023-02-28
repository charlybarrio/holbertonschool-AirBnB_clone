#!/usr/bin/python3
'''create a class user'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Define a user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
