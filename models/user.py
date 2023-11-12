#!/usr/bin/python3
"""User class definition."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel.
    Attributes:
        email: user email.
        password: user password.
        first_name: first name of the user.
        last_name: last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
