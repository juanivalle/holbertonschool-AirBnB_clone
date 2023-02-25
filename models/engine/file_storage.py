#!/usr/bin/python3
"""comments"""


import json
from models.base_model import BaseModel
import os.path


class FileStorage:
    """comments"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """comments"""

        return self.__objects

    def new(self, obj):
        """comments"""

        if obj is not None:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """comments"""

        with open(self.__file_path, 'w') as f:
            objects_json = {}
            for key, value in self.__objects.items():
                objects_json[key] = value.to_dict()
            json.dump(objects_json, f)

    def reload(self):
        """comments"""
        dicc1 = {}
        
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                for key, value in json.load(f).items():
                    mt = str(key).split(".")
                    if mt[0] in dicc1.keys():
                        self.__objects[key] = dicc1[mt[0]](**value)
        except FileNotFoundError:
            pass
