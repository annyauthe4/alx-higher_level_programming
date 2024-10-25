import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Unit test for the Base class."""

    def setUp(self):
        """Resets the __nb_objects counter before each test
        to ensure tests are independent.
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_base_with_id(self):
        """Test creating Base instance with a specified id."""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_base_without_id(self):
        """Test creating Base instance without providing id."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_mixed_id(self):
        """Test creating Base instance with and without id."""
        b1 = Base()
        b2 = Base()
        b3 = Base(14)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 14)
        self.assertEqual(b4.id, 3)

    def test_private_nb_objects(self):
        """Tests that __nb_objects is a private attr and can not
        accessed directly.
        """
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.__nb_objects)

    def test_to_json_string(self):
        """Test to JSON string conversion method."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, result)

    def test_to_json_empty(self):
        """Test an empty argument with to_json_string."""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_str_none(self):
        """Test to_json_string with None."""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_save_to_file_Rectangle(self):
        """Test saving Rectangle obj in save_to_file."""
        r = Rectangle(10, 5, 2, 3, id=1)
        r1 = Rectangle(7, 8, id=2)
        Rectangle.save_to_file([r, r1])

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
        expected = Base.to_json_string(
            [r.to_dictionary(), r1.to_dictionary()]
        )
        self.assertEqual(expected, content)

    def test_save_to_file_Square(self):
        """Test saving Square instance to file."""
        s = Square(10, 2, 2, id=1)
        s1 = Square(5, id=2)
        Square.save_to_file([s, s1])

        with open("Square.json", "r", encoding="utf-8") as file:
            content = file.read()
        expected = Base.to_json_string(
            [s.to_dictionary(), s1.to_dictionary()]
        )
        self.assertEqual(content, expected)

    def test_save_to_file_empty(self):
        """Test saving empty list to a file."""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_None(self):
        """Test saving none to a file."""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, "[]")


if __name__ == "__main__":
    unittest.main()
