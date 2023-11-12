#!/usr/bin/python3
"""unittests for models/base_model.py.

Unittest classes names:
    Test_BaseModel_init
    Test_BaseModel_save
    Test_BaseModel_to_dict
"""
import os
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
from time import sleep


class Test_BaseModel_init(unittest.TestCase):
    """testing instantiation of the BaseModel class."""
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_args_unused(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_f = _datetime.isoformat()
        base_model = BaseModel(id="abc123", created_at=iso_f, updated_at=iso_f)
        self.assertEqual(base_model.id, "abc123")
        self.assertEqual(base_model.created_at, _datetime)
        self.assertEqual(base_model.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        _datetime = datetime.today()
        iso_f = _datetime.isoformat()
        basm = BaseModel("7", id="a7", created_at=iso_f, updated_at=iso_f)
        self.assertEqual(basm.id, "a7")
        self.assertEqual(basm.created_at, _datetime)
        self.assertEqual(basm.updated_at, _datetime)

    def test_new_instance_stored_in_object(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_two_models_different_created_at(self):
        base_model1 = BaseModel()
        sleep(0.05)
        base_model2 = BaseModel()
        self.assertLess(base_model1.created_at, base_model2.created_at)

    def test_two_models_different_updated_at(self):
        base_model1 = BaseModel()
        sleep(0.05)
        base_model2 = BaseModel()
        self.assertLess(base_model1.updated_at, base_model2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        datetime_rep = repr(_datetime)
        base_model = BaseModel()
        base_model.id = "abcd1234"
        base_model.created_at = base_model.updated_at = _datetime
        base_model_str = base_model.__str__()
        self.assertIn("[BaseModel] (abcd1234)", base_model_str)
        self.assertIn("'id': 'abcd1234'", base_model_str)
        self.assertIn("'created_at': " + datetime_rep, base_model_str)
        self.assertIn("'updated_at': " + datetime_rep, base_model_str)


class Test_BaseModel_save(unittest.TestCase):
    """testing save method of the BaseModel class."""
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

    def test_one_save(self):
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(first_updated_at, base_model.updated_at)

    def test_two_saves(self):
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        second_updated_at = base_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_model.save()
        self.assertLess(second_updated_at, base_model.updated_at)

    def test_save_with_arg(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def test_save_updates_file(self):
        base_model = BaseModel()
        base_model.save()
        base_model_id = "BaseModel." + base_model.id
        with open("file.json", "r") as f:
            self.assertIn(base_model_id, f.read())


class Test_BaseModel_to_dict(unittest.TestCase):
    """testing to_dict method of the BaseModel class."""
    def test_to_dict_type(self):
        base_model = BaseModel()
        self.assertTrue(dict, type(base_model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        base_model = BaseModel()
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

    def test_to_dict_contains_added_attributes(self):
        base_model = BaseModel()
        base_model.name = "Morocco"
        base_model.country_code = 212
        self.assertIn("name", base_model.to_dict())
        self.assertIn("country_code", base_model.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        base_model = BaseModel()
        base_model.id = "11"
        base_model.created_at = base_model.updated_at = _datetime
        test_dict = {
            'id': '11',
            '__class__': 'BaseModel',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), test_dict)

    def test_contrast_to_dict_dunder_dict(self):
        base_model = BaseModel()
        self.assertNotEqual(base_model.to_dict(), base_model.__dict__)

    def test_to_dict_with_arg(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)


if __name__ == '__main__':
    unittest.main()
