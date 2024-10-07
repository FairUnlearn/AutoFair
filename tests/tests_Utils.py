import unittest
import coverage 

from src.autofair.Utils import get_distance

class TestGetDistance(unittest.TestCase):

    def test_get_distance(self):
        self.assertEqual(get_distance(0, 0, 3, 4), 5.0)

    def test_get_distance_negative(self):
        self.assertEqual(get_distance(0, 0, -3, -4), 5.0)
