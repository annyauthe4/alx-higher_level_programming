import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit test for the Base class."""

    def setUp(self):
        """Resets the __nb_objects counter before each test
        to ensure tests are independent.
        """
        Base._Base__nb_objects = 0

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


if __name__ == "__main__":
    unittest.main()
