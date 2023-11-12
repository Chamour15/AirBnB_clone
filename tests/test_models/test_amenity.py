#!/usr/bin/python3
"""unittests for models/amenity.py.
Unittest classes names:
    Test_Amenity_init
    Test_Amenity_save
    Test_Amenity_to_dict
"""
import unittest
import models
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import os


class Test_Amenity_init(unittest.TestCase):
    """testing instantiation of the Amenity class."""
    def test_no_args_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_args_unused(self):
        new_amenity = Amenity(None)
        self.assertNotIn(None, new_amenity.__dict__.values())

    def test_new_instance_stored_in_object(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        new_amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", new_amenity.__dict__)

    def test_two_amenities_unique_ids(self):
        new_amenity1 = Amenity()
        new_amenity2 = Amenity()
        self.assertNotEqual(new_amenity1.id, new_amenity2.id)

    def test_two_amenities_different_created_at(self):
        new_amenity1 = Amenity()
        sleep(0.05)
        new_amenity2 = Amenity()
        self.assertLess(new_amenity1.created_at, new_amenity2.created_at)

    def test_two_amenities_different_updated_at(self):
        new_amenity1 = Amenity()
        sleep(0.05)
        new_amenity2 = Amenity()
        self.assertLess(new_amenity1.updated_at, new_amenity2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        dt_repr = repr(_datetime)
        new_amenity = Amenity()
        new_amenity.id = "1111"
        new_amenity.created_at = new_amenity.updated_at = _datetime
        new_amenity_str = new_amenity.__str__()
        self.assertIn("[Amenity] (1111)", new_amenity_str)
        self.assertIn("'id': '1111'", new_amenity_str)
        self.assertIn("'created_at': " + dt_repr, new_amenity_str)
        self.assertIn("'updated_at': " + dt_repr, new_amenity_str)

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_f = _datetime.isoformat()
        new_amenity = Amenity(id="11", created_at=iso_f, updated_at=iso_f)
        self.assertEqual(new_amenity.id, "11")
        self.assertEqual(new_amenity.created_at, _datetime)
        self.assertEqual(new_amenity.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class Test_Amenity_save(unittest.TestCase):
    """testing save method of the Amenity class."""
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

    def test_one_save(self):
        new_amenity = Amenity()
        sleep(0.05)
        first_updated_at = new_amenity.updated_at
        new_amenity.save()
        self.assertLess(first_updated_at, new_amenity.updated_at)

    def test_two_saves(self):
        new_amenity = Amenity()
        sleep(0.05)
        first_updated_at = new_amenity.updated_at
        new_amenity.save()
        second_updated_at = new_amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        new_amenity.save()
        self.assertLess(second_updated_at, new_amenity.updated_at)

    def test_save_with_arg(self):
        new_amenity = Amenity()
        with self.assertRaises(TypeError):
            new_amenity.save(None)

    def test_save_updates_file(self):
        new_amenity = Amenity()
        new_amenity.save()
        amid = "Amenity." + new_amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class Test_Amenity_to_dict(unittest.TestCase):
    """testing to_dict method of the Amenity class."""
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        new_amenity = Amenity()
        self.assertIn("id", new_amenity.to_dict())
        self.assertIn("created_at", new_amenity.to_dict())
        self.assertIn("updated_at", new_amenity.to_dict())
        self.assertIn("__class__", new_amenity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        new_amenity = Amenity()
        new_amenity.feature = "pleasure"
        new_amenity.code = 212
        self.assertEqual("pleasure", new_amenity.feature)
        self.assertIn("code", new_amenity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        new_amenity = Amenity()
        amenity_dict = new_amenity.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        new_amenity = Amenity()
        new_amenity.id = "11"
        new_amenity.created_at = new_amenity.updated_at = _datetime
        tdict = {
            'id': '11',
            '__class__': 'Amenity',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat(),
        }
        self.assertDictEqual(new_amenity.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        new_amenity = Amenity()
        self.assertNotEqual(new_amenity.to_dict(), new_amenity.__dict__)

    def test_to_dict_with_arg(self):
        new_amenity = Amenity()
        with self.assertRaises(TypeError):
            new_amenity.to_dict(None)


if __name__ == '__main__':
    unittest.main()
