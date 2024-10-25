import unittest
from models.base import Base
from models.rectangle import Rectangle


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


if __name__ == "__main__":
    unittest.main()
