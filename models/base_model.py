#!/usr/bin/python3
"""
Base Model
"""
import uuid
from datetime import datetime


class BaseModel:
    """basemodel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        return "[{}] ({}) ({})".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        update_at = datetime.now()

    def to_dict(self):
        Base_dict = {
                "id": self.id,
                "created_at": self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                "update_at": self.update_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                "__class__": type(self).__name__,
                }
        return Base_dict
