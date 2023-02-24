#!/usr/bin/python3
"""comments"""

import datetime
import uuid
from models import storage

class BaseModel:
    """comments"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        """comments"""
        return(f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """comments"""

        self.updated_at = datetime.datetime.now()
        storage.save()
    
    def to_dict(self):
        """comments"""

        dicc = self.__dict__.copy()
        dicc["__class__"] = type(self).__name__
        dicc["created_at"] = self.created_at.isoformat()
        dicc["updated_at"] = self.updated_at.isoformat()
        return dicc

    def __init__(self, *args, **kwargs):
        """comments"""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.datetime.now()
                    self.updated_at = datetime.datetime.now()
                    storage.new(self)
