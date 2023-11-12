#!/usr/bin/python3
"""unittests for models/user.py.
Unittest classes names:
    Test_User_init
    Test_User_save
    Test_User_to_dict
"""
import models
from models.user import User
import os
import unittest
from datetime import datetime
from time import sleep


class Test_User_init(unittest.TestCase):
    """testing instantiation of the User class."""
    def test_args_unused(self):
        new_user = User(None)
        self.assertNotIn(None, new_user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_format = _datetime.isoformat()
        new_user = User(id="4", created_at=iso_format, updated_at=iso_format)
        self.assertEqual(new_user.id, "4")
        self.assertEqual(new_user.created_at, _datetime)
        self.assertEqual(new_user.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        new_use1 = User()
        new_use2 = User()
        self.assertNotEqual(new_use1.id, new_use2.id)

    def test_two_users_different_created_at(self):
        new_use1 = User()
        sleep(0.05)
        new_use2 = User()
        self.assertLess(new_use1.created_at, new_use2.created_at)

    def test_two_users_different_updated_at(self):
        new_use1 = User()
        sleep(0.05)
        new_use2 = User()
        self.assertLess(new_use1.updated_at, new_use2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        datetime_repre = repr(_datetime)
        new_use = User()
        new_use.id = "1177"
        new_use.created_at = new_use.updated_at = _datetime
        user_str = new_use.__str__()
        self.assertIn("[User] (1177)", user_str)
        self.assertIn("'id': '1177'", user_str)
        self.assertIn("'created_at': " + datetime_repre, user_str)
        self.assertIn("'updated_at': " + datetime_repre, user_str)


class Test_User_save(unittest.TestCase):
    """testing save method of the User class."""
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
        new_user = User()
        with self.assertRaises(TypeError):
            new_user.save(None)

    def test_one_save(self):
        new_user = User()
        sleep(0.05)
        first_updated_at = new_user.updated_at
        new_user.save()
        self.assertLess(first_updated_at, new_user.updated_at)

    def test_two_saves(self):
        new_user = User()
        sleep(0.05)
        first_updated_at = new_user.updated_at
        new_user.save()
        second_updated_at = new_user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        new_user.save()
        self.assertLess(second_updated_at, new_user.updated_at)

    def test_save_updates_file(self):
        new_user = User()
        new_user.save()
        user_id = "User." + new_user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class Test_User_to_dict(unittest.TestCase):
    """testing to_dict method of the User class."""
    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        new_user = User()
        self.assertIn("id", new_user.to_dict())
        self.assertIn("created_at", new_user.to_dict())
        self.assertIn("updated_at", new_user.to_dict())
        self.assertIn("__class__", new_user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        new_user = User()
        new_user.first_name = "Wafae"
        new_user.user_number = 1
        self.assertEqual("Wafae", new_user.first_name)
        self.assertIn("user_number", new_user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        new_user = User()
        new_user.id = "7711"
        new_user.created_at = new_user.updated_at = _datetime
        test_dict = {
            'id': '7711',
            '__class__': 'User',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat(),
        }
        self.assertDictEqual(new_user.to_dict(), test_dict)

    def test_contrast_to_dict_dunder_dict(self):
        new_user = User()
        self.assertNotEqual(new_user.to_dict(), new_user.__dict__)

    def test_to_dict_with_arg(self):
        new_user = User()
        with self.assertRaises(TypeError):
            new_user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
