#!/usr/bin/python3
"""Module for the HBNB console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State", "City",
                "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id"""
        if line == "":
            print("** class name missing **")
            return
        if line not in self.classes:
            print("** class doesn't exist **")
            return
        if line == "BaseModel":
            obj = BaseModel()
        elif line == "User":
            obj = User()
        elif line == "Place":
            obj = Place()
        elif line == "State":
            obj = State()
        elif line == "City":
            obj = City()
        elif line == "Amenity":
            obj = Amenity()
        elif line == "Review":
            obj = Review()
        storage.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of instances"""
        objects = storage.all()
        if not arg:
            print([str(objects[key]) for key in objects])
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(objects[key]) for key in objects if arg in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[3], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
