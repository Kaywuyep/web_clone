#!/usr/bin/python3
""" Unittest for User class """
import unittest
import json
import pycodestyle
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """my test cases"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review()

    def test_pep8_compliance(self):
        """check if the code adheres to the pep8 guidelines"""
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test document string in the file user.py"""
        self.assertIsNotNone(Review.__doc__)

    def test_isInstance(self):
        """Test for instantiation in the file"""
        self.assertIsInstance(self.review, Review)

    def test_default_attributes(self):
        """Test default attribute values"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attributes_after_update(self):
        """Test updating attributes"""
        self.review.place_id = ""
        self.review.user_id = ""
        self.review.text = ""

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attributes(self):
        """Test attribute initialization"""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_save_method(self):
        """Test save method"""
        initial_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(initial_updated_at, self.review.updated_at)
