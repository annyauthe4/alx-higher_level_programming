import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittest for the square class."""

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
