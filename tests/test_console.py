#!/usr/bin/python3
"""Defines unittests for console.py"""
import unittest
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch
import sys
import os
from io import StringIO
from models import storage
from models.user import User


class TestConsole(unittest.TestCase):

    def setup(self):
        storage. Reload()


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB"""

    def test_help_quit(self):
        msg = 'Quit command to exit the program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            self.assertEqual(f.getvalue(), msg)


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command"""

    def test_update_missing_attr_value_dot_notation(self):
        correct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()

    def test_update_valid_string_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "update User {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        self.assertEqual(" 'attr_value' ", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            tId = output.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "update BaseModel {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_all_users(self):
        user1 = User(id=1, email='test1@test.com', password='test1')
        user2 = User(id=2, email='test2@test.com', password='test2')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            self.assertEqual(f.getvalue(), str(user1) + '\n' + str(user2))


if __name__ == "__main__":
    unittest.main()
