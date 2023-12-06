#!/usr/bin/python3
"""a unit test for my base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up common objects for test cases"""
        self.model = BaseModel()

    def test_init(self):
        """Test the initialization of BaseModel instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test the save method of BaseModel"""
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual\
            (model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual\
            (model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        str_representation = str(self.model)
        self.assertIsInstance(str_representation, str)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(self.model.id, str_representation)
        self.assertIn(str(self.model.__dict__), str_representation)
