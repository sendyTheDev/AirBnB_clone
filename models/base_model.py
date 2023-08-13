#!/usr/bin/python3
"""
This class defines all common attributes/methods for other classes
"""
from datetime import datetime
import models
import uuid
import json


class BaseModel:
    """Base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if kwargs:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'name' in kwargs:
                self.name = kwargs['name']
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_Number']
            if 'created_at' in kwargs:
                self.created_at = (
                        datetime
                        .strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                        )
            else:
                self.created_at = datetime.today()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.today()
        else:
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def save(self):
        """This method is to update self"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Return to the simple representation of our BaseModel"""
        str = "[{}] ({}) {}"
        return str.format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns  a dict containing
           all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict['created_at'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['updated_at'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict.update({'__class__': self.__class__.__name__})
        return my_dict
