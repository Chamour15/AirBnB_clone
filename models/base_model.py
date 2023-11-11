#!/usr/bin/python3
"""BaseModel class definition for all common attributes/methods
for other classes.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel of all instances."""
    def __init__(self, *args, **kwargs):
        """initialize new BaseModel.

        Args:
            *args: unused.
            **kwargs: Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, iso_format)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """print BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at,
        with the current time.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        re_dict = self.__dict__.copy()
        re_dict["created_at"] = self.created_at.isoformat()
        re_dict["updated_at"] = self.updated_at.isoformat()
        re_dict["__class__"] = self.__class__.__name__
        return re_dict
