#!/usr/bin/python3
""" class User that inherits from BaseModel"""
import models

class User(BaseModel):
    """a simple user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
