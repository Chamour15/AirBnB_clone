#!/usr/bin/python3
"""unittests for models/engine/file_storage.py.
Unittest classes names:
    Test_FileStorage_instantiation
    Test_FileStorage_methods
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_FileStorage_instantiation(unittest.TestCase):
    """testing instantiation of the FileStorage class."""
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorage_methods(unittest.TestCase):
    """testing methods of the FileStorage class."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_model = BaseModel()
        user = User()
        state = State()
        amenity = Amenity()
        place = Place()
        city = City()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn("BaseModel." + base_model.id, models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        base_model = BaseModel()
        new_user = User()
        new_state = State()
        new_amenity = Amenity()
        new_place = Place()
        new_city = City()
        new_review = Review()
        models.storage.new(base_model)
        models.storage.new(new_user)
        models.storage.new(new_state)
        models.storage.new(new_place)
        models.storage.new(new_city)
        models.storage.new(new_amenity)
        models.storage.new(new_review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + new_user.id, save_text)
            self.assertIn("State." + new_state.id, save_text)
            self.assertIn("Place." + new_place.id, save_text)
            self.assertIn("City." + new_city.id, save_text)
            self.assertIn("Amenity." + new_amenity.id, save_text)
            self.assertIn("Review." + new_review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        new_base_model = BaseModel()
        new_user = User()
        new_state = State()
        new_place = Place()
        new_city = City()
        new_amenity = Amenity()
        new_review = Review()
        models.storage.new(new_base_model)
        models.storage.new(new_user)
        models.storage.new(new_state)
        models.storage.new(new_place)
        models.storage.new(new_city)
        models.storage.new(new_amenity)
        models.storage.new(new_review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + new_base_model.id, objs)
        self.assertIn("User." + new_user.id, objs)
        self.assertIn("State." + new_state.id, objs)
        self.assertIn("Place." + new_place.id, objs)
        self.assertIn("City." + new_city.id, objs)
        self.assertIn("Amenity." + new_amenity.id, objs)
        self.assertIn("Review." + new_review.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
