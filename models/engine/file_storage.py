#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """erializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {}
            for key, obj in FileStorage.__objects.items():
                new_dict[key] = obj.to_dict()
            json.dump(new_dict, fname)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path) as f:
                deserialized = json.load(f)
                for object_data in deserialized.values():
                    cls_name = object_data["__class__"]
                    del object_data["__class__"]
                    self.new(eval(cls_name)(**object_data))
        except FileNotFoundError:
            pass
