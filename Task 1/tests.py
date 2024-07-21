import unittest
from main import Circle, Triangle, area_in_compile_time


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(first=area_in_compile_time(circle), second=78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(first=area_in_compile_time(triangle), second=6.0)

    def test_triangle_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

        triangle2 = Triangle(2, 2, 3)
        self.assertFalse(triangle2.is_right_angled())


if __name__ == '__main__':
    unittest.main()
