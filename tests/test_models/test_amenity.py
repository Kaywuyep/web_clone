#!/usr/bin/python3
"""a unit test for my amenity module"""
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


class TestAmenity(unittest.TestCase):
    """my test cases"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.amenity = Amenity()

    def test_pep8_compliance(self):
        """check if the code adheres to the pep8 guidelines"""
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test document string in the file user.py"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_isInstance(self):
        """Test for instantiation in the file"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test attribute initialization"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_save_method(self):
        """Test save method"""
        initial_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(initial_updated_at, self.amenity.updated_at)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes"""
        initial_created_at = self.amenity.created_at
        initial_updated_at = self.amenity.updated_at

        # Simulate a delay
        self.amenity.save()
        updated_created_at = self.amenity.created_at
        updated_updated_at = self.amenity.updated_at

        self.assertEqual(initial_created_at, updated_created_at)
        self.assertNotEqual(initial_updated_at, updated_updated_at)


#if __name__ == '__main__':
 #   unittest.main()
