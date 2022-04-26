import unittest
from calculator import addition, substraction

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(addition(1,3), 4, "Should be 4")

    def test_sum_tuple(self):
        self.assertEqual(addition(3, 4), 7, "Should be 6")

class TestSubstraction(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(substraction(4,9), -5, "Should be -4")

    def test_sum_tuple(self):
        self.assertEqual(addition(9,0), 9, "Should be 9")

if __name__ == '__main__':

    unittest.main()