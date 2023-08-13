#!/usr/bin/python3
"""
This class defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """Base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert string to datetime
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.today()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.today()
        else:
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            self.id = str(uuid.uuid4())
 
    def save(self):
        """This method is to update self"""
        from models import storage
        self.updated_at = datetime.today()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Return to the simple representation of our BaseModel"""
        str = "[{}] ({}) {}"
        return str.format(self.__class__.__name__, self.id, self.__dict__)
