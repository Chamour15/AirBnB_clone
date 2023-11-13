#!/usr/bin/python3
"""unittests for console.py.
Unittest classes names:
    Test_HBNBCommand_prompt
    Test_HBNBCommand_create
    Test_HBNBCommand_show
    Test_HBNBCommand_destroy
    Test_HBNBCommand_all
    Test_HBNBCommand_update
    Test_HBNBCommand_count
    Test_HBNBCommand_help
    Test_HBNBCommand_exit
"""
import unittest
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
import os
import sys
from io import StringIO
from unittest.mock import patch


class Test_HBNBCommand_prompt(unittest.TestCase):
    """testing HBNBCommand interpreter prompt."""
    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class Test_HBNBCommand_create(unittest.TestCase):
    """testing create from the HBNBCommand interpreter."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(response, output.getvalue().strip())

    def test_create_invalid_class(self):
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Street"))
            self.assertEqual(response, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        response = "*** Unknown syntax: Street.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Street.create()"))
            self.assertEqual(response, output.getvalue().strip())
        response = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "User.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "City.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "State.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """testing show from the HBNBCommand interpreter."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_show_invalid_class(self):
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Town"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Town.show()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_show_missing_id_space_character(self):
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(response, output.getvalue().strip())

    def test_show_missing_id_dot_character(self):
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_show_no_instance_found_space_character(self):
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 7"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 111"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 5"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 22"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 13"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 71"))
            self.assertEqual(response, output.getvalue().strip())

    def test_show_no_instance_found_dot_character(self):
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(113)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(232)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(41)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(8)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(4)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(2)"))
            self.assertEqual(response, output.getvalue().strip())

    def test_show_objects_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["BaseModel.{}".format(ID)]
            command = "show BaseModel {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["User.{}".format(ID)]
            command = "show User {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Place.{}".format(ID)]
            command = "show Place {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["State.{}".format(ID)]
            command = "show State {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["City.{}".format(ID)]
            command = "show City {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Amenity.{}".format(ID)]
            command = "show Amenity {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Review.{}".format(ID)]
            command = "show Review {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(_object.__str__(), output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """testing destroy from the HBNBCommand interpreter."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self):
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Street"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Street.destroy()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_id_missing_space_character(self):
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_id_missing_dot_character(self):
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_invalid_id_space_character(self):
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 7"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 3"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 2"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 11"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 8"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 13"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_invalid_id_dot_character(self):
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(76)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(11)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(13)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(5)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(6)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(7)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_objects_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["BaseModel.{}".format(ID)]
            command = "destroy BaseModel {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["User.{}".format(ID)]
            command = "show User {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["City.{}".format(ID)]
            command = "show City {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Amenity.{}".format(ID)]
            command = "show Amenity {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["State.{}".format(ID)]
            command = "show State {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Place.{}".format(ID)]
            command = "show Place {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Review.{}".format(ID)]
            command = "show Review {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())

    def test_destroy_objects_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["BaseModel.{}".format(ID)]
            command = "BaseModel.destroy({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["User.{}".format(ID)]
            command = "User.destroy({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["City.{}".format(ID)]
            command = "City.destroy({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Amenity.{}".format(ID)]
            command = "Amenity.destroy({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["State.{}".format(ID)]
            command = "State.destroy({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Place.{}".format(ID)]
            command = "Place.destroy({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            _object = storage.all()["Review.{}".format(ID)]
            command = "Review.destory({})".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(_object, storage.all())


class Test_HBNBCommand_all(unittest.TestCase):
    """testing all command of HBNBCommand interpreter."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Street"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Street.all()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_all_objects_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objects_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_single_object_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class Test_HBNBCommand_update(unittest.TestCase):
    """testing update from the HBNBCommand interpreter."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class(self):
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_invalid_class(self):
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_missing_id_space_character(self):
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_missing_id_dot_character(self):
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_invalid_id_space_character(self):
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_invalid_id_dot_character(self):
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_missing_attr_name_space_character(self):
        response = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ID = output.getvalue().strip()
            command = "update BaseModel {}".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            ID = output.getvalue().strip()
            command = "update User {}".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ID = output.getvalue().strip()
            command = "update State {}".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            ID = output.getvalue().strip()
            command = "update City {}".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            ID = output.getvalue().strip()
            command = "update Amenity {}".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            ID = output.getvalue().strip()
            command = "update Place {}".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_missing_attr_name_dot_character(self):
        response = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ID = output.getvalue().strip()
            command = "BaseModel.update({})".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            ID = output.getvalue().strip()
            command = "User.update({})".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ID = output.getvalue().strip()
            command = "State.update({})".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            ID = output.getvalue().strip()
            command = "City.update({})".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            ID = output.getvalue().strip()
            command = "Amenity.update({})".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            ID = output.getvalue().strip()
            command = "Place.update({})".format(ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_missing_attr_value_space_character(self):
        response = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update BaseModel {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update User {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update City {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update State {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Amenity {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Place {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "update Review {} attr_name".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_missing_attr_value_dot_character(self):
        response = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "BaseModel.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "User.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "State.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "City.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "Amenity.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "Place.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "Review.update({}, attr_name)".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_valid_string_attr_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            ID = output.getvalue().strip()
        command = "update BaseModel {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["BaseModel.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            ID = output.getvalue().strip()
        command = "update User {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["User.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            ID = output.getvalue().strip()
        command = "update City {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["City.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            ID = output.getvalue().strip()
        command = "update Amenity {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Amenity.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            ID = output.getvalue().strip()
        command = "update State {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["State.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "update Place {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            ID = output.getvalue().strip()
        command = "update Review {} attr_name 'attr_value'".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Review.{}".format(ID)].__dict__
        self.assertTrue("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attr_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            ID = output.getvalue().strip()
        command = "BaseModel.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["BaseModel.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            ID = output.getvalue().strip()
        command = "User.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["User.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            ID = output.getvalue().strip()
        command = "City.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["City.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            ID = output.getvalue().strip()
        command = "Amenity.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Amenity.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            ID = output.getvalue().strip()
        command = "State.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["State.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "Place.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            ID = output.getvalue().strip()
        command = "Review.update({}, attr_name, 'attr_value')".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Review.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attr_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "update Place {} max_guest 100".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(100, test_dict["max_guest"])

    def test_update_valid_int_attr_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "Place.update({}, max_guest, 100)".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(100, test_dict["max_guest"])

    def test_update_valid_float_attr_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "update Place {} latitude 4.0".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(4.0, test_dict["latitude"])

    def test_update_valid_float_attr_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "Place.update({}, latitude, 4.0)".format(ID)
        self.assertFalse(HBNBCommand().onecmd(command))
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(4.0, test_dict["latitude"])

    def test_update_valid_dictionary_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            ID = output.getvalue().strip()
        command = "update BaseModel {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["BaseModel.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            ID = output.getvalue().strip()
        command = "update User {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["User.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            ID = output.getvalue().strip()
        command = "update State {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["State.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            ID = output.getvalue().strip()
        command = "update City {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["City.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "update Place {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            ID = output.getvalue().strip()
        command = "update Amenity {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Amenity.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            ID = output.getvalue().strip()
        command = "update Review {} ".format(ID)
        command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Review.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            ID = output.getvalue().strip()
        command = "BaseModel.update({}".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["BaseModel.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            ID = output.getvalue().strip()
        command = "User.update({}, ".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["User.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            ID = output.getvalue().strip()
        command = "State.update({}, ".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["State.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            ID = output.getvalue().strip()
        command = "City.update({}, ".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["City.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "Place.update({}, ".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            ID = output.getvalue().strip()
        command = "Amenity.update({}, ".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Amenity.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            ID = output.getvalue().strip()
        command = "Review.update({}, ".format(ID)
        command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Review.{}".format(ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "update Place {} ".format(ID)
        command += "{'max_guest': 100})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(100, test_dict["max_guest"])

    def test_update_valid_dictionary_with_int_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "Place.update({}, ".format(ID)
        command += "{'max_guest': 100})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(100, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_space_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "update Place {} ".format(ID)
        command += "{'latitude': 4.7})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(4.7, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_character(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            ID = output.getvalue().strip()
        command = "Place.update({}, ".format(ID)
        command += "{'latitude': 4.7})"
        HBNBCommand().onecmd(command)
        test_dict = storage.all()["Place.{}".format(ID)].__dict__
        self.assertEqual(4.7, test_dict["latitude"])


class Test_HBNBCommand_count(unittest.TestCase):
    """testing count method of HBNBComand interpreter."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Street.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


class Test_HBNBCommand_help(unittest.TestCase):
    """testing help messages of the HBNBCommand interpreter."""
    def test_help_create(self):
        msg = ("Creates a new instance of BaseModel, saves it "
               "(to the JSON file)\n        "
               "and prints the id. Usage: $ create BaseModel")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_show(self):
        msg = ("Prints the string representation of an instance based"
               " on the class\n        "
               "name and id. Usage: $ show BaseModel 1234-1234-1234.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_destroy(self):
        msg = ("Deletes an instance based on the class name and id "
               "(save the change\n        "
               "into the JSON file). "
               "Usage: $ destroy BaseModel 1234-1234-1234")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_all(self):
        msg = ("Prints all string representation of all "
               "instances based or not on\n        "
               "the class name. Usage: $ all BaseModel or $ all")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_count(self):
        msg = ("retrieve the number of instances of a class.\n        "
               "Usage: (hbnb) User.count()")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_update(self):
        msg = ("Updates an instance based on the class name and id\n        "
               "by adding or updating attribute"
               " (save the change into the JSON file).\n        "
               "Usage: "
               "update <class name> <id> <attribute name> <attribute value>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help(self):
        msg = ("Documented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_quit(self):
        msg = "Quit command to exit the console."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_EOF(self):
        msg = "EOF signal to exit the console."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(msg, output.getvalue().strip())


class Test_HBNBCommand_exit(unittest.TestCase):
    """testing exiting from the HBNBCommand interpreter."""
    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
