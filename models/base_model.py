#!/usr/bin/python3

"""
This file defines  the BaseModel class which will
serve as the base of our model.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initializes a new base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
