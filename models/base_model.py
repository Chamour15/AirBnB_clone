#!/usr/bin/python3
"""BaseModel class definition for all common attributes/methods for other cls"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save (self):
        self.updated_at = datetime.today()

    def to_dict(self):
        re_dict = self.__dict__.copy()
        re_dict["created_at"] = self.created_at.isoformat()
        re_dict["updated_at"] = self.updated_at.isoformat()
        re_dict["__class__"] = self.__class__.__name__
        return re_dict
