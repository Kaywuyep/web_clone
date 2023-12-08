#!/usr/bin/python3
""" Unittest for User class """
import unittest
import json
import pycodestyle
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """my test cases"""
    def setUp(self):
        """set up commom user for test cases"""
        self.user = User()

    def test_pep8_compliance(self):
        """check if the code adheres to the pep8 guidelines"""
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test document string in the file user.py"""
        self.assertIsNotNone(User.__doc__)

    def test_isInstance(self):
        """Test for instantiation in the file"""
        self.assertIsInstance(self.user, User)

    def test_default_attributes(self):
        """Test default attribute values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attributes_after_update(self):
        """Test updating attributes"""
        self.user.email = "test@alx.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Smith"

        self.assertEqual(self.user.email, "test@alx.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Smith")

    def test_attributes(self):
        """Test to check attributes"""
        self.user.save()
        user_json = self.user.to_dict()
        new_user = User(**user_json)
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)
        self.assertIsNot(self.user, new_user)

    def test_subclass(self):
        """Test to check the inheritance, if it is True"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method in the file"""
        updated_variable = self.user.updated_at
        self.user.save()
        self.assertNotEqual(updated_variable, self.user.updated_at)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes"""
        initial_created_at = self.user.created_at
        initial_updated_at = self.user.updated_at

        # Simulate a delay
        self.user.save()
        updated_created_at = self.user.created_at
        updated_updated_at = self.user.updated_at

        self.assertEqual(initial_created_at, updated_created_at)
        self.assertNotEqual(initial_updated_at, updated_updated_at)


if __name__ == '__main__':
    unittest.main()
