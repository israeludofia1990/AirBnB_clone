#!/usr/bin/python3
# Created by Israel Udofia & Emmanuel Ademola

"""Unittest for place.py"""

import unittest
import models
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Test suites"""

    def test_place_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_subclass(self):
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
