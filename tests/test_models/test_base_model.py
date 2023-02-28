#!/usr/bin/python3
import unittest
from datetime import datetime
from models import storage
import uuid
from models.base_model import BaseModel

'''test base model module'''


class TestBaseModel(unittest.TestCase):
    '''class to test the BaseModel class'''
    def test_cases_base_model(self):
        my_obj = BaseModel()
        my_obj.name = 'Name'
        my_obj.number = 13
        my_obj.save()
        my_obj_dict = my_obj.to_dict()
        self.assertEqual(my_obj.name, 'Name')
        self.assertEqual(my_obj.number, 13)
        self.assertEqual(my_obj.__class__.__name__, 'BaseModel')
        self.assertEqual(isinstance(my_obj.created_at, datetime), True)
        self.assertEqual(isinstance(my_obj.updated_at, datetime), True)
        self.assertEqual(type(my_obj.__dict__), dict)

if __name__ == "__main__":
    unittest.main()
