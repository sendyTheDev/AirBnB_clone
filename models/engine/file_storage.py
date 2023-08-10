#!/usr/bin/python3
"""
thi class that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def save(self):
        """ it Serializes __objects to the JSON file (path: __file_path)"""
        temp_dictionary = self.__objects
        object_dictionary = {obj: temp_dictionary[obj].to_dict() for obj in temp_dictionary.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(object_dictionary, file)

    def new(self, obj):
        """it Sets in the obj with key <obj class name>.id in __objects
        Args:
            obj (BaseModel): Object to be added
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def reload(self):
        """it deserializes the JSON file to __objects if file exists"""
        try:
            with open(self.__file_path, "r") as storeFile:
                obj_dict = json.load(storeFile)
                for b in obj_dict.values():
                    class_name = b["__class__"]
                    del b["__class__"]
                    self.new(eval(class_name)(**b))
        except FileNotFoundError:
            return
