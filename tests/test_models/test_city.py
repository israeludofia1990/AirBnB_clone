#!/usr/bin/python3
# Created by Israel Udofia & Emmanuel Ademola

"""Unittest for city.py"""

import unittest
import models
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """Test suites"""

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_subclass(self):
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
