import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unittest for the square class."""

    def setUp(self):
        """Resets id to zero after each test."""
        Base._Base__nb_objects = 0

    def test_square_initialization(self):
        """Test initializing square with rectangle init method."""
        s = Square(4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_square_with_arguments(self):
        """Test square initialization with arguments."""
        s = Square(5, 2, 3, 15)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 15)

    def test_square_with_setter(self):
        """Test initializing square with setter."""
        s = Square(15, 20)
        s.width = 12
        s.height = 10
        s.x = 5
        s.y = 8
        self.assertEqual(s.width, 12)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 8)

    def test_square_str(self):
        """Test square class string method."""
        s = Square(10, 2, 3, 15)
        self.assertEqual(str(s), "[Square] (15) 2/3 - 10")

    def test_square_area(self):
        """Test square area from Rectangle area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_getter(self):
        """Returns square size."""
        s = Square(17)
        self.assertEqual(s.size, 17)

    def test_square_setter(self):
        """Test the setter for square."""
        s = Square(5)
        s.size = 25
        self.assertEqual(s.width, 25)
        self.assertEqual(s.height, 25)

    def test_square_invalid_size(self):
        """Test invalid size input."""
        with self.assertRaises(TypeError):
            Square("6")
        with self.assertRaises(ValueError):
            Square(-6)

    def test_square_update_method(self):
        """Test the square update method."""
        s = Square(5)
        s.update(10, 5, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_with_kwargs(self):
        """Test the update method with kwargs."""
        s = Square(6, 2, 7, 10)
        s.update(size=8, x=9, y=11, id=12)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 9)
        self.assertEqual(s.y, 11)
        self.assertEqual(s.id, 12)

    def test_to_dictionary(self):
        """Test dict rep of object method."""
        s = Square(10, 2, 3)
        result = {'size': 10, 'x': 2, 'y': 3, 'id': 1}
        self.assertEqual(s.to_dictionary(), result)


if __name__ == "__main__":
    unittest.main()
