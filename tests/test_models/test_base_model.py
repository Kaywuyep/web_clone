#!/usr/bin/python3
"""a unit test for my base model"""
import sys
import os
import models
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def setUp(self):
        """
        Set up a new instance of BaseModel for each test case
        """
        self.my_model = BaseModel()

    def test_attributes(self):
        """
        Test that id, created_at, and updated_at are present
        """
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_save_method(self):
        """
        Test that save method updates updated_at
        """
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method for expected keys and values
        """
        my_model_dict = self.my_model.to_dict()
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        """
        Test the __str__ method for expected output
        """
        str_output = str(self.my_model)
        self.assertIn('BaseModel', str_output)
        self.assertIn(self.my_model.id, str_output)
