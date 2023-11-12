#!/usr/bin/python3
"""unittests for models/place.py.
Unittest classes names:
    Test_Place_init
    Test_Place_save
    Test_Place_to_dict
"""
import unittest
import models
import os
from models.place import Place
from datetime import datetime
from time import sleep


class Test_Place_init(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""
    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_args_unused(self):
        new_place = Place(None)
        self.assertNotIn(None, new_place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_format = _datetime.isoformat()
        new_place = Place(id="7", created_at=iso_format, updated_at=iso_format)
        self.assertEqual(new_place.id, "7")
        self.assertEqual(new_place.created_at, _datetime)
        self.assertEqual(new_place.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(new_place))
        self.assertNotIn("city_id", new_place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(new_place))
        self.assertNotIn("user_id", new_place.__dict__)

    def test_name_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(new_place))
        self.assertNotIn("name", new_place.__dict__)

    def test_description_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(new_place))
        self.assertNotIn("desctiption", new_place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(new_place))
        self.assertNotIn("number_rooms", new_place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(new_place))
        self.assertNotIn("number_bathrooms", new_place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(new_place))
        self.assertNotIn("max_guest", new_place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(new_place))
        self.assertNotIn("price_by_night", new_place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(new_place))
        self.assertNotIn("latitude", new_place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(new_place))
        self.assertNotIn("longitude", new_place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        new_place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(new_place))
        self.assertNotIn("amenity_ids", new_place.__dict__)

    def test_two_places_unique_ids(self):
        new_place1 = Place()
        new_place2 = Place()
        self.assertNotEqual(new_place1.id, new_place2.id)

    def test_two_places_different_created_at(self):
        new_place1 = Place()
        sleep(0.05)
        new_place2 = Place()
        self.assertLess(new_place1.created_at, new_place2.created_at)

    def test_two_places_different_updated_at(self):
        new_place1 = Place()
        sleep(0.05)
        new_place2 = Place()
        self.assertLess(new_place1.updated_at, new_place2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        datetime_representation = repr(_datetime)
        new_place = Place()
        new_place.id = "1177"
        new_place.created_at = new_place.updated_at = _datetime
        place_str = new_place.__str__()
        self.assertIn("[Place] (1177)", place_str)
        self.assertIn("'id': '1177'", place_str)
        self.assertIn("'created_at': " + datetime_representation, place_str)
        self.assertIn("'updated_at': " + datetime_representation, place_str)


class Test_Place_save(unittest.TestCase):
    """testing save method of the Place class."""
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
        new_place = Place()
        with self.assertRaises(TypeError):
            new_place.save(None)

    def test_one_save(self):
        new_place = Place()
        sleep(0.05)
        first_updated_at = new_place.updated_at
        new_place.save()
        self.assertLess(first_updated_at, new_place.updated_at)

    def test_two_saves(self):
        new_place = Place()
        sleep(0.05)
        first_updated_at = new_place.updated_at
        new_place.save()
        second_updated_at = new_place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        new_place.save()
        self.assertLess(second_updated_at, new_place.updated_at)

    def test_save_updates_file(self):
        new_place = Place()
        new_place.save()
        place_id = "Place." + new_place.id
        with open("file.json", "r") as f:
            self.assertIn(place_id, f.read())


class Test_Place_to_dict(unittest.TestCase):
    """testing to_dict method of the Place class."""
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_with_arg(self):
        new_place = Place()
        with self.assertRaises(TypeError):
            new_place.to_dict(None)

    def test_to_dict_contains_correct_keys(self):
        new_place = Place()
        self.assertIn("id", new_place.to_dict())
        self.assertIn("created_at", new_place.to_dict())
        self.assertIn("updated_at", new_place.to_dict())
        self.assertIn("__class__", new_place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        new_place = Place()
        new_place.pname = "Hotel"
        new_place.room = 98
        self.assertEqual("Hotel", new_place.pname)
        self.assertIn("room", new_place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        new_place = Place()
        place_dict = new_place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        new_place = Place()
        new_place.id = "1177"
        new_place.created_at = new_place.updated_at = _datetime
        test_dict = {
            'id': '1177',
            '__class__': 'Place',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat(),
        }
        self.assertDictEqual(new_place.to_dict(), test_dict)

    def test_contrast_to_dict_dunder_dict(self):
        new_place = Place()
        self.assertNotEqual(new_place.to_dict(), new_place.__dict__)


if __name__ == '__main__':
    unittest.main()
