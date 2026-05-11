#!/usr/bin/python3
"""Unittest for Base, Rectangle and Square"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        s = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 1}])


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def test_basic(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_xy(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("a", 2)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "a")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "a")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 0, "a")

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -1)

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)

    def test_update_kwargs(self):
        r = Rectangle(10, 10)
        r.update(width=5, height=3)
        self.assertEqual(r.width, 5)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def test_basic(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("a")

    def test_size_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_update_args(self):
        s = Square(5)
        s.update(10, 3, 1, 2)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 3)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, x=1)
        self.assertEqual(s.size, 7)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)


if __name__ == '__main__':
    unittest.main()
