#!/usr/bin/python3
"""
This class defines all common attributes/methods for other classes
"""
import datetime
import uuid
import models


class BaseModel:
    """Base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(args) > 0:
            for x in args[0]:
                setattr(self, x, args[0][x])
        else:
            self.created_at = datetime.today()
            self.id = str(uuid.uuid4())
        for x in kwargs:
            print("kwargs: {}: {}".format(x, kwargs[x]))

    def save(self):
        """This method is to update self"""
        self.updated_at = datetime.datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Return to the simple representation of our BaseModel"""
        return "[{}] ({}) {}" \
                .format(self.__class__.__name__, self.id, self.__dict__)
