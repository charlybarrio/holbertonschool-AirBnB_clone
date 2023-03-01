#!/usr/bin/python3
"""
Base Model
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """basemodel"""
    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{type(self).__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        base_dict = self.__dict__.copy()
        Base_dict = {
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": type(self).__name__,
                }
        return Base_dict
