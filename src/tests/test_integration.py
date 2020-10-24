import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):   
        self.assertEqual(add(3,5), 8)
