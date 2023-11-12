#!/usr/bin/python3
# Created by Israel Udofia & Emmanuel Ademola

"""Unittest for state.py"""

import unittest
import models
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """Test suites"""

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
