#!/usr/bin/python3
"""comments"""

import datetime
import uuid

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
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """comments"""
        dicc = self.__dict__.copy()
        dicc["__class__"] = type(self).__name__
        dicc["created_at"] = self.created_at.isoformat()
        dicc["update_at"] = self.update_at.isoformat()
        return dicc