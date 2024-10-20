import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit test for the rectangle class"""

    def setUp(self):
        """Resets the private class attribute of the Base class"""
        Rectangle._Base__nb_objects = 0

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


if __name__ == "__main__":
     unittest.main()
