#!/usr/bin/python3
"""unittests for models/city.py.
Unittest classes names:
    Test_City_init
    Test_City_save
    Test_City_to_dict
"""
import os
import unittest
import models
from models.city import City
from datetime import datetime
from time import sleep


class Test_City_init(unittest.TestCase):
    """testing instantiation of the City class."""
    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_args_unused(self):
        new_city = City(None)
        self.assertNotIn(None, new_city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_format = _datetime.isoformat()
        new_city = City(id="7", created_at=iso_format, updated_at=iso_format)
        self.assertEqual(new_city.id, "7")
        self.assertEqual(new_city.created_at, _datetime)
        self.assertEqual(new_city.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_new_instance_stored_in_object(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        new_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(new_city))
        self.assertNotIn("state_id", new_city.__dict__)

    def test_name_is_public_class_attribute(self):
        new_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(new_city))
        self.assertNotIn("name", new_city.__dict__)

    def test_two_cities_unique_ids(self):
        new_city1 = City()
        new_city2 = City()
        self.assertNotEqual(new_city1.id, new_city2.id)

    def test_two_cities_different_created_at(self):
        new_city1 = City()
        sleep(0.05)
        new_city2 = City()
        self.assertLess(new_city1.created_at, new_city2.created_at)

    def test_two_cities_different_updated_at(self):
        new_city1 = City()
        sleep(0.05)
        new_city2 = City()
        self.assertLess(new_city1.updated_at, new_city2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        datetime_representation = repr(_datetime)
        new_city = City()
        new_city.id = "11"
        new_city.created_at = new_city.updated_at = _datetime
        city_str = new_city.__str__()
        self.assertIn("[City] (11)", city_str)
        self.assertIn("'id': '11'", city_str)
        self.assertIn("'created_at': " + datetime_representation, city_str)
        self.assertIn("'updated_at': " + datetime_representation, city_str)


class Test_City_save(unittest.TestCase):
    """testing save method of the City class."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        new_city = City()
        with self.assertRaises(TypeError):
            new_city.save(None)

    def test_one_save(self):
        new_city = City()
        sleep(0.05)
        first_updated_at = new_city.updated_at
        new_city.save()
        self.assertLess(first_updated_at, new_city.updated_at)

    def test_two_saves(self):
        new_city = City()
        sleep(0.05)
        first_updated_at = new_city.updated_at
        new_city.save()
        second_updated_at = new_city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        new_city.save()
        self.assertLess(second_updated_at, new_city.updated_at)

    def test_save_updates_file(self):
        new_city = City()
        new_city.save()
        new_city_id = "City." + new_city.id
        with open("file.json", "r") as f:
            self.assertIn(new_city_id, f.read())


class Test_City_to_dict(unittest.TestCase):
    """testing to_dict method of the City class."""
    def test_to_dict_with_arg(self):
        new_city = City()
        with self.assertRaises(TypeError):
            new_city.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        new_city = City()
        self.assertIn("id", new_city.to_dict())
        self.assertIn("created_at", new_city.to_dict())
        self.assertIn("updated_at", new_city.to_dict())
        self.assertIn("__class__", new_city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        new_city = City()
        new_city.middle_name = "Holberton"
        new_city.my_number = 98
        self.assertEqual("Holberton", new_city.middle_name)
        self.assertIn("my_number", new_city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        new_city = City()
        new_city_dict = new_city.to_dict()
        self.assertEqual(str, type(new_city_dict["id"]))
        self.assertEqual(str, type(new_city_dict["created_at"]))
        self.assertEqual(str, type(new_city_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        new_city = City()
        new_city.id = "7"
        new_city.created_at = new_city.updated_at = _datetime
        tdict = {
            'id': '7',
            '__class__': 'City',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat(),
        }
        self.assertDictEqual(new_city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        new_city = City()
        self.assertNotEqual(new_city.to_dict(), new_city.__dict__)


if __name__ == '__main__':
    unittest.main()
