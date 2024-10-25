from models.base import Base
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Unit test for the rectangle class"""

    def setUp(self):
        """Resets the private class attribute of the Base class"""
        Base._Base__nb_objects = 0

    def test_rectangle_instance(self):
        """Test if rectangle instance is created with the right attr"""
        r1 = Rectangle(4, 12, 3, 7, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 7)

    def test_rectangle_default_id(self):
        """Test that id is auto-assigned when not provided."""
        r = Rectangle(10, 20)
        b = Rectangle(12, 18)
        self.assertEqual(r.id, 1)
        self.assertEqual(b.id, 2)

    def test_setter_getter(self):
        """Test the setters and getters for width, height, x and y."""
        r = Rectangle(12, 15)
        r.width = 10
        r.height = 20
        r.x = 30
        r.y = 40
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)


    def test_invalid_width(self):
        """Test for invalid width input."""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "15"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_invalid_height(self):
        """Test setting invalid height raises error."""
        r = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            r.height = [13]
        with self.assertRaises(ValueError):
            r.height = 0

    def test_invalid_x(self):
        """Test setting invalid x raises error"""
        r = Rectangle(13, 15)
        with self.assertRaises(TypeError):
            r.x = 5.5
        with self.assertRaises(ValueError):
            r.x = -5

    def test_invalid_y(self):
        """Test setting invalid y raises error."""
        r = Rectangle(10, 30)
        with self.assertRaises(TypeError):
            r.y = "10"
        with self.assertRaises(ValueError):
            r.y = -8

    def test_area(self):
        """Test the area method of the rectangle class."""
        r = Rectangle(5, 4, 0, 0, 2)
        self.assertEqual(r.area(), 20)
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)

    def test_area_with_setter_getter(self):
        """Test area method using setter-getter method."""
        r = Rectangle(4, 6)
        r.width = 3
        r.height = 4
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """Test display method of the rectangle instance class."""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_y(self):
        """Test display method with x and y coordinates."""
        r = Rectangle(3, 4, 2, 1)
        expected = "\n  ###\n  ###\n  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_setter(self):
        """Test display method using setter method"""
        r = Rectangle(5, 4)
        r.width = 2
        r.height = 3
        r.x = 2
        r.y = 1
        expected_out = "\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_out)

    def test_str_method(self):
        """Test the __str__ method of the Rectangle class."""
        r = Rectangle(4, 5, 1, 2, 6)
        expected = "[Rectangle] (6) 1/2 - 4/5"
        self.assertEqual(str(r), expected)

    def test_str_with_auto_id(self):
        """Test __str__ method with auto id generation."""
        r = Rectangle(3, 6, 4, 5)
        expected = "[Rectangle] (1) 4/5 - 3/6"
        self.assertEqual(str(r), expected)

    def test_str_with_setter(self):
        """Test __str__ method with setter."""
        r = Rectangle(10, 15)
        r.width = 5
        r.height = 7
        r.x = 4
        r.y = 9
        expected = "[Rectangle] (1) 4/9 - 5/7"
        self.assertEqual(str(r), expected)

    def test_update_attributes(self):
        """Test the update attributes."""
        r = Rectangle(3, 4, 5, 6)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_with_less_arg(self):
        """Test update method with args."""
        r = Rectangle(2, 3, 4, 5)
        r.update(54)
        self.assertEqual(r.id, 54)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_with_kwargs(self):
        """Test update method with kwargs."""
        r = Rectangle(3, 4, 5, 6)
        r.update(id=10, width=20, height=30, x=40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        """Test class to dictionary method."""
        r = Rectangle(3, 4, 5, 6)
        result = {
            'width': 3, 'height': 4, 'x': 5, 'y': 6, 'id': 1
        }
        self.assertEqual(r.to_dictionary(), result)


if __name__ == "__main__":
     unittest.main()
