#!/usr/bin/python3

"""
Test Cases for the console Module
"""

import cmd
import unittest
from console import HBNBCommand
from io import StringIO
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models import storage
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """
    Tests all the methods and functions in the console module
    """
    """
    TESTING DOCUMENTATION OF EACH METHOD
    """
    def test_help_quit(self):
        """
        Help doc for quit
        """
        output = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_EOF(self):
        """
        Help doc for EOF
        """
        output = "End of File Method - Quit program"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_create(self):
        """
        Help doc for create
        """
        output = "Creates a new instance of BaseModel and prints the id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_show(self):
        """
        Help doc for show
        """
        output = "Prints the string representation of an instance"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_destroy(self):
        """
        Help doc for destroy
        """
        output = "Deletes an instance based on the class name and id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_all(self):
        """
        Help doc for all
        """
        output = "Prints all string representation of all instances"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_update(self):
        """
        Help doc for update
        """
        output = "Updates an instance based on the class name and id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(), output)

    def test_help_count(self):
        """
        Help doc for count
        """
        output = "Retrieves the number of instances of a class"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue().strip(), output)

    """
    TESTING FUNCTIONALITY OF EACH METHOD
    """
    def test_emptyline(self):
        """
        Tests the empty line function
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_do_quit(self):
        """
        Tests the program exit
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_do_EOF(self):
        """
        Tests the End of File function - exits program
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_do_create_no_class_name(self):
        """
        creates a new instance
        """
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), output)

    def test_do_create_invalid_class_name(self):
        """
        creates a new instance
        """
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Base")
            self.assertEqual(f.getvalue(), output)

    def test_do_create_class_name(self):
        """
        creates a new instance
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(type(f.getvalue()), str)

    def test_do_show_no_class_name(self):
        """
        Prints the object string representation
        """
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), output)

    def test_do_show_invalid_class_name(self):
        """
        Prints the object string representation
        """
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "show Use 49faff9a-6318-451f-87b6-910505c55907")
            self.assertEqual(f.getvalue(), output)

    def test_do_show_no_id(self):
        """
        Prints the object string representation
        """
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), output)

    def test_do_show_invalid_id(self):
        """
        Prints the object string representation
        """
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 12345")
            self.assertEqual(f.getvalue(), output)

    def test_do_show(self):
        """
        Prints the object string representation
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "show BaseModel 49faff9a-6318-451f-87b6-910505c55907")
            self.assertTrue(type(f.getvalue()), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "BaseModel.show(49faff9a-6318-451f-87b6-910505c55907)")
            self.assertTrue(type(f.getvalue()), str)

    def test_do_destroy_no_class_name(self):
        """
        Deletes an object instance
        """
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), output)

    def test_do_destroy_invalid_class_name(self):
        """
        Deletes an object instance
        """
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "destroy Plac 49faff9a-6318-451f-87b6-910505c55907")
            self.assertEqual(f.getvalue(), output)

    def test_do_destroy_invalid_no_id(self):
        """
        Deletes an object instance
        """
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("delete Review")
            self.assertEqual(f.getvalue(), output)

    def test_do_destroy(self):
        """
        Deletes an object instance
        """
        x = "delete BaseModel 49faff9a-6318-451f-87b6-910505c55907"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(x)
            self.assertTrue(type(f.getvalue()), "")

        y = "User.delete('49faff9a-6318-451f-87b6-910505c55907')"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(y)
            self.assertTrue(type(f.getvalue()), "")

    def test_do_all_no_class_name(self):
        """
        Prints all string representation of all instances
        """
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Plaxz")
            self.assertEqual(f.getvalue(), output)

    def test_do_all(self):
        """
        Prints all string representation of all instances
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(type(f.getvalue()), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue(type(f.getvalue()), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertTrue(type(f.getvalue()), str)

    def test_do_count(self):
        """
        Prints the number of objects
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertTrue(type(f.getvalue()), int)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(type(f.getvalue()), int)

    def test_do_update_no_class_name(self):
        """
        Updates an object
        """
        output = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), output)

    def test_do_update_invalid_class_name(self):
        """
        Updates an object
        """
        output = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "update Use 49faff9a-6318-451f-87b6-910505c55907")
            self.assertEqual(f.getvalue(), output)

    def test_do_update_no_id(self):
        """
        Updates an object
        """
        output = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                    "update User")
            self.assertEqual(f.getvalue(), output)

    def test_do_update_invalid_id(self):
        """
        Updates an object instance
        """
        output = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 12345")
            self.assertEqual(f.getvalue(), output)

    def test_do_update(self):
        """
        Updates an object
        """
        x = "update BaseModel 49faff9a-6318-451f-87b6-910505c55907 a b"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(x)
            self.assertTrue(type(f.getvalue()), str)

        y = "User.update('49faff9a-6318-451f-87b6-910505c55907',\
                'a', 'b')"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(y)
            self.assertTrue(type(f.getvalue()), str)
