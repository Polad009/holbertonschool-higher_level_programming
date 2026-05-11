python3 << 'PYEOF'
content = '''#!/usr/bin/python3
"""Unittest for Base, Rectangle and Square"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        """Test of Base() for assigning automatically an ID"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_auto_increment(self):
        """Test of Base() for assigning automatically an ID + 1 of the previous"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        """Test of Base(89) saving the ID passed"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test of Base.to_json_string(None)"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test of Base.to_json_string([])"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test of Base.to_json_string([ { \'id\': 12 }])"""
        result = Base.to_json_string([{"id": 12}])
        self.assertEqual(json.loads(result), [{"id": 12}])

    def test_to_json_string_returns_string(self):
        """Test of Base.to_json_string([ { \'id\': 12 }]) returning a string"""
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """Test of Base.from_json_string(None)"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test of Base.from_json_string("[]")"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        """Test of Base.from_json_string(\'[{ "id": 89 }]\')"""
        result = Base.from_json_string(\'[{ "id": 89 }]\')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Test of Base.from_json_string(\'[{ "id": 89 }]\') returning a list"""
        result = Base.from_json_string(\'[{ "id": 89 }]\')
        self.assertIsInstance(result, list)


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rect_1_2(self):
        """Test of Rectangle(1, 2)"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_rect_1_2_3(self):
        """Test of Rectangle(1, 2, 3)"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rect_1_2_3_4(self):
        """Test of Rectangle(1, 2, 3, 4)"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rect_str_width(self):
        """Test of Rectangle("1", 2)"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rect_str_height(self):
        """Test of Rectangle(1, "2")"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rect_str_x(self):
        """Test of Rectangle(1, 2, "3")"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rect_str_y(self):
        """Test of Rectangle(1, 2, 3, "4")"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rect_1_2_3_4_5(self):
        """Test of Rectangle(1, 2, 3, 4, 5)"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rect_neg_width(self):
        """Test of Rectangle(-1, 2)"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rect_neg_height(self):
        """Test of Rectangle(1, -2)"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rect_zero_width(self):
        """Test of Rectangle(0, 2)"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rect_zero_height(self):
        """Test of Rectangle(1, 0)"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rect_neg_x(self):
        """Test of Rectangle(1, 2, -3)"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rect_neg_y(self):
        """Test of Rectangle(1, 2, 3, -4)"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test of area()"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test of __str__() for Rectangle"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_y(self):
        """Test of display() without x and y"""
        import io
        from unittest.mock import patch
        r = Rectangle(2, 2)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_out:
            r.display()
            self.assertEqual(mock_out.getvalue(), "##\\n##\\n")

    def test_display_no_y(self):
        """Test of display() without y"""
        import io
        from unittest.mock import patch
        r = Rectangle(2, 2, 1)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_out:
            r.display()
            self.assertEqual(mock_out.getvalue(), " ##\\n ##\\n")

    def test_display(self):
        """Test of display()"""
        import io
        from unittest.mock import patch
        r = Rectangle(2, 2, 1, 1)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_out:
            r.display()
            self.assertEqual(mock_out.getvalue(), "\\n ##\\n ##\\n")

    def test_to_dictionary(self):
        """Test of to_dictionary() in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4})

    def test_update(self):
        """Test of update() in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.id, 5)

    def test_update_89(self):
        """Test of update(89) in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test of update(89, 1) in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2(self):
        """Test of update(89, 1, 2) in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4(self):
        """Test of update(89, 1, 2, 3, 4) in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        """Test of update(**{ \'id\': 89 }) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test of update(**{ \'id\': 89, \'width\': 1 }) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        """Test of update(**{ \'id\': 89, \'width\': 1, \'height\': 2 }) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        """Test of update(**{ \'id\': 89, \'width\': 1, \'height\': 2, \'x\': 3 }) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_all(self):
        """Test of update(**{ \'id\': 89, \'width\': 1, \'height\': 2, \'x\': 3, \'y\': 4 }) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        """Test of Rectangle.create(**{ \'id\': 89 }) in Rectangle"""
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Test of Rectangle.create(**{ \'id\': 89, \'width\': 1 }) in Rectangle"""
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Test of Rectangle.create(**{ \'id\': 89, \'width\': 1, \'height\': 2 }) in Rectangle"""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Test of Rectangle.create(**{ \'id\': 89, \'width\': 1, \'height\': 2, \'x\': 3 }) in Rectangle"""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r.x, 3)

    def test_create_all(self):
        """Test of Rectangle.create(**{ \'id\': 89, \'width\': 1, \'height\': 2, \'x\': 3, \'y\': 4 }) in Rectangle"""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test of Rectangle.save_to_file(None) in Rectangle"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Rectangle.save_to_file([]) in Rectangle"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(data[0]["width"], 1)

    def test_load_from_file_no_file(self):
        """Test of Rectangle.load_from_file() when file doesn\'t exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Test of Rectangle.load_from_file() when file exists"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        result = Rectangle.load_from_file()
        self.assertIsInstance(result[0], Rectangle)


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_1(self):
        """Test of Square(1)"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        """Test of Square(1, 2)"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        """Test of Square(1, 2, 3)"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_str_size(self):
        """Test of Square("1")"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_str_x(self):
        """Test of Square(1, "2")"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_str_y(self):
        """Test of Square(1, 2, "3")"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        """Test of Square(1, 2, 3, 4)"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_neg_size(self):
        """Test of Square(-1)"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_neg_x(self):
        """Test of Square(1, -2)"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_neg_y(self):
        """Test of Square(1, 2, -3)"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero(self):
        """Test of Square(0)"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_square(self):
        """Test of __str__() for Square"""
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_to_dictionary_square(self):
        """Test of to_dictionary() in Square"""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.to_dictionary(), {"id": 10, "size": 5, "x": 1, "y": 2})

    def test_update_square(self):
        """Test of update() in Square"""
        s = Square(5, 1, 2, 10)
        s.update()
        self.assertEqual(s.id, 10)

    def test_update_square_89(self):
        """Test of update(89) in Square"""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_square_89_1(self):
        """Test of update(89, 1) in Square"""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_square_89_1_2(self):
        """Test of update(89, 1, 2) in Square"""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_square_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Square"""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_square_kwargs_id(self):
        """Test of update(**{ \'id\': 89 }) in Square"""
        s = Square(5)
        s.update(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_update_square_kwargs_size(self):
        """Test of update(**{ \'id\': 89, \'size\': 1 }) in Square"""
        s = Square(5)
        s.update(**{"id": 89, "size": 1})
        self.assertEqual(s.size, 1)

    def test_update_square_kwargs_x(self):
        """Test of update(**{ \'id\': 89, \'size\': 1, \'x\': 2 }) in Square"""
        s = Square(5)
        s.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s.x, 2)

    def test_update_square_kwargs_y(self):
        """Test of update(**{ \'id\': 89, \'size\': 1, \'x\': 2, \'y\': 3 }) in Square"""
        s = Square(5)
        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(s.y, 3)

    def test_create_square_id(self):
        """Test of Square.create(**{ \'id\': 89 }) in Square"""
        s = Square.create(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_create_square_size(self):
        """Test of Square.create(**{ \'id\': 89, \'size\': 1 }) in Square"""
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(s.size, 1)

    def test_create_square_x(self):
        """Test of Square.create(**{ \'id\': 89, \'size\': 1, \'x\': 2 }) in Square"""
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s.x, 2)

    def test_create_square_y(self):
        """Test of Square.create(**{ \'id\': 89, \'size\': 1, \'x\': 2, \'y\': 3 }) in Square"""
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none_square(self):
        """Test of Square.save_to_file(None) in Square"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_square(self):
        """Test of Square.save_to_file([]) in Square"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square(self):
        """Test of Square.save_to_file([Square(1)]) in Square"""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(data[0]["size"], 1)

    def test_load_from_file_no_file_square(self):
        """Test of Square.load_from_file() when file doesn\'t exist"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_square(self):
        """Test of Square.load_from_file() when file exists"""
        Square.save_to_file([Square(1)])
        result = Square.load_from_file()
        self.assertIsInstance(result[0], Square)


if __name__ == "__main__":
    unittest.main()
'''

with open("tests/test_models.py", "w") as f:
    f.write(content)
print("Done!")
