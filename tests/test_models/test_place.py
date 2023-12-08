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


class TestPlace(unittest.TestCase):
    """my test cases"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.place = Place()

    def test_pep8_compliance(self):
        """check if the code adheres to the pep8 guidelines"""
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test document string in the file user.py"""
        self.assertIsNotNone(Place.__doc__)

    def test_isInstance(self):
        """Test for instantiation in the file"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test attribute initialization"""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_save_method(self):
        """Test save method"""
        initial_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(initial_updated_at, self.place.updated_at)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes"""
        initial_created_at = self.place.created_at
        initial_updated_at = self.place.updated_at

        # Simulate a delay
        self.place.save()
        updated_created_at = self.place.created_at
        updated_updated_at = self.place.updated_at

        self.assertEqual(initial_created_at, updated_created_at)
        self.assertNotEqual(initial_updated_at, updated_updated_at)


#if __name__ == '__main__':
  #  unittest.main()
