#!/usr/bin/python3
# Created by Israel Udofia & Emmanuel Ademola

"""Unittest for user.py"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test suites"""

    def test_user_attributes(self):
        user = User()

        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
