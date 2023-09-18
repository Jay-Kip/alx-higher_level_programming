#!/usr/bin/python3


import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
        """Unittests for testing instantiation of the Rectangle class."""
        def test_rectangle_is_base(self):
            self.assertIsInstance(Rectangle(10, 2), Base)

        def test_no_args(self):
            with self.assertRaises(TypeError):
                Rectangle()

        def test_rect_one_arg(self):
            with self.assertRaises(TypeError):
                Rectangle(1)

        def test_rect_two_args(self):
            rect_1 = Rectangle(2, 3)
            rect_2 = Rectangle(3, 2)
            self.assertEqual(rect_1.id, rect_2.id - 1)
