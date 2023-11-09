#!/usr/bin/python3
"""State class definition."""
from models.base_model import BaseModel


class State(BaseModel):
    """state class inherits from BaseModel.
    Attributes:
        name: name of the state.
    """

    name = ""
