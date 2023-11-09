#!/usr/bin/python3
"""City class definition."""
from models.base_model import BaseModel


class City(BaseModel):
    """city class inherits from BaseModel.
    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """

    state_id = ""
    name = ""
