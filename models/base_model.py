#!/usr/bin/python3
"""comments"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """comments"""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
    
    def __str__(self):
        """comments"""
        return(f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """comments"""

        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """comments"""

    def to_dict(self):
        """ Return a dictonary """
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict