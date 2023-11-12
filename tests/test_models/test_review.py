#!/usr/bin/python3
# Created by Israel Udofia & Emmanuel Ademola

"""Unittest for review.py"""

import unittest
import models
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test suites"""

    def test_review_attributes(self):
        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))

    def test_subclass(self):
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
