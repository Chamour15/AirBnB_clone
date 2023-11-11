#!/usr/bin/python3
"""unittests for models/review.py.
Unittest classes names:
    Test_Review_init
    Test_Review_save
    Test_Review_to_dict
"""
import unittest
import models
from models.review import Review
from datetime import datetime
from time import sleep
import os


class Test_Review_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""
    def test_args_unused(self):
        new_review = Review(None)
        self.assertNotIn(None, new_review.__dict__.values())

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_instantiation_with_kwargs(self):
        _datetime = datetime.today()
        iso_f = _datetime.isoformat()
        new_review = Review(id="1", created_at=iso_f, updated_at=iso_f)
        self.assertEqual(new_review.id, "1")
        self.assertEqual(new_review.created_at, _datetime)
        self.assertEqual(new_review.updated_at, _datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        new_review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(new_review))
        self.assertNotIn("place_id", new_review.__dict__)

    def test_user_id_is_public_class_attribute(self):
        new_review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(new_review))
        self.assertNotIn("user_id", new_review.__dict__)

    def test_text_is_public_class_attribute(self):
        new_review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(new_review))
        self.assertNotIn("text", new_review.__dict__)

    def test_two_reviews_unique_ids(self):
        new_review1 = Review()
        new_review2 = Review()
        self.assertNotEqual(new_review1.id, new_review2.id)

    def test_two_reviews_different_created_at(self):
        new_review1 = Review()
        sleep(0.05)
        new_review2 = Review()
        self.assertLess(new_review1.created_at, new_review2.created_at)

    def test_two_reviews_different_updated_at(self):
        new_review1 = Review()
        sleep(0.05)
        new_review2 = Review()
        self.assertLess(new_review1.updated_at, new_review2.updated_at)

    def test_str_representation(self):
        _datetime = datetime.today()
        datetime_repre = repr(_datetime)
        new_review = Review()
        new_review.id = "1111"
        new_review.created_at = new_review.updated_at = _datetime
        review_str = new_review.__str__()
        self.assertIn("[Review] (1111)", review_str)
        self.assertIn("'id': '1111'", review_str)
        self.assertIn("'created_at': " + datetime_repre, review_str)
        self.assertIn("'updated_at': " + datetime_repre, review_str)


class Test_Review_save(unittest.TestCase):
    """testing save method of the Review class."""
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
        new_review = Review()
        with self.assertRaises(TypeError):
            new_review.save(None)

    def test_one_save(self):
        new_review = Review()
        sleep(0.05)
        first_updated_at = new_review.updated_at
        new_review.save()
        self.assertLess(first_updated_at, new_review.updated_at)

    def test_two_saves(self):
        new_review = Review()
        sleep(0.05)
        first_updated_at = new_review.updated_at
        new_review.save()
        second_updated_at = new_review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        new_review.save()
        self.assertLess(second_updated_at, new_review.updated_at)

    def test_save_updates_file(self):
        new_review = Review()
        new_review.save()
        review_id = "Review." + new_review.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


class Test_Review_to_dict(unittest.TestCase):
    """testing to_dict method of the Review class."""
    def test_to_dict_with_arg(self):
        new_review = Review()
        with self.assertRaises(TypeError):
            new_review.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        new_review = Review()
        self.assertIn("id", new_review.to_dict())
        self.assertIn("created_at", new_review.to_dict())
        self.assertIn("updated_at", new_review.to_dict())
        self.assertIn("__class__", new_review.to_dict())

    def test_to_dict_contains_added_attributes(self):
        new_review = Review()
        new_review.name = "DAKHA"
        new_review.number = 11
        self.assertEqual("DAKHA", new_review.name)
        self.assertIn("number", new_review.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        new_review = Review()
        review_dict = new_review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        _datetime = datetime.today()
        new_review = Review()
        new_review.id = "777777"
        new_review.created_at = new_review.updated_at = _datetime
        test_dict = {
            'id': '777777',
            '__class__': 'Review',
            'created_at': _datetime.isoformat(),
            'updated_at': _datetime.isoformat(),
        }
        self.assertDictEqual(new_review.to_dict(), test_dict)

    def test_contrast_to_dict_dunder_dict(self):
        new_review = Review()
        self.assertNotEqual(new_review.to_dict(), new_review.__dict__)


if __name__ == '__main__':
    unittest.main()
