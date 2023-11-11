#!/usr/bin/python3
"""unittests for models/state.py.
Unittest classes name:
    Test_State_init
    Test_State_save
    Test_State_to_dict
"""
import unittest
from models.state import State
import os
import models
from datetime import datetime
from time import sleep


class Test_State_instantiation(unittest.TestCase):
    """testing instantiation of the State class."""
    def test_args_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_format = _datetime.isoformat()
        st = State(id="20", created_at=iso_format, updated_at=iso_format)
        self.assertEqual(st.id, "20")
        self.assertEqual(st.created_at, _datetime)
        self.assertEqual(st.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        new_state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(new_state))
        self.assertNotIn("name", new_state.__dict__)

    def test_two_states_unique_ids(self):
        new_state1 = State()
        new_state2 = State()
        self.assertNotEqual(new_state1.id, new_state2.id)

    def test_two_states_different_created_at(self):
        new_state1 = State()
        sleep(0.05)
        new_state2 = State()
        self.assertLess(new_state1.created_at, new_state2.created_at)

    def test_two_states_different_updated_at(self):
        new_state1 = State()
        sleep(0.05)
        new_state2 = State()
        self.assertLess(new_state1.updated_at, new_state2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        datetime_repres = repr(_datetime)
        new_state = State()
        new_state.id = "20"
        new_state.created_at = new_state.updated_at = _datetime
        state_str = new_state.__str__()
        self.assertIn("[State] (20)", state_str)
        self.assertIn("'id': '20'", state_str)
        self.assertIn("'created_at': " + datetime_repres, state_str)
        self.assertIn("'updated_at': " + datetime_repres, state_str)


class Test_State_save(unittest.TestCase):
    """testing save method of the State class."""
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
        new_state = State()
        sleep(0.05)
        first_updated_at = new_state.updated_at
        new_state.save()
        self.assertLess(first_updated_at, new_state.updated_at)

    def test_two_saves(self):
        new_state = State()
        sleep(0.05)
        first_updated_at = new_state.updated_at
        new_state.save()
        second_updated_at = new_state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        new_state.save()
        self.assertLess(second_updated_at, new_state.updated_at)

    def test_save_with_arg(self):
        new_state = State()
        with self.assertRaises(TypeError):
            new_state.save(None)

    def test_save_updates_file(self):
        new_state = State()
        new_state.save()
        state_id = "State." + new_state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


class Test_State_to_dict(unittest.TestCase):
    """testing to_dict method of the State class."""
    def test_to_dict_with_arg(self):
        new_state = State()
        with self.assertRaises(TypeError):
            new_state.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        new_state = State()
        self.assertIn("id", new_state.to_dict())
        self.assertIn("created_at", new_state.to_dict())
        self.assertIn("updated_at", new_state.to_dict())
        self.assertIn("__class__", new_state.to_dict())

    def test_to_dict_contains_added_attributes(self):
        new_state = State()
        new_state.name = "Rabat"
        new_state.state_number = 1
        self.assertEqual("Rabat", new_state.name)
        self.assertIn("state_number", new_state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        new_state = State()
        state_dict = new_state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        new_state = State()
        new_state.id = "1"
        new_state.created_at = new_state.updated_at = _datetime
        test_dict = {
            'id': '1',
            '__class__': 'State',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat(),
        }
        self.assertDictEqual(new_state.to_dict(), test_dict)

    def test_contrast_to_dict_dunder_dict(self):
        new_state = State()
        self.assertNotEqual(new_state.to_dict(), new_state.__dict__)


if __name__ == "__main__":
    unittest.main()
