import unittest
from karate_chop import chop_iterative

class TestIterativeChop(unittest.TestCase):

    def test_small_cases(self):
        self.assertEqual(-1, chop_iterative(3, []))
        self.assertEqual(-1, chop_iterative(3, [1]))
        self.assertEqual(0,  chop_iterative(1, [1]))
    def test_three_items(self):    
        self.assertEqual(0,  chop_iterative(1, [1, 3, 5]))
        self.assertEqual(1,  chop_iterative(3, [1, 3, 5]))
        self.assertEqual(2,  chop_iterative(5, [1, 3, 5]))
        self.assertEqual(-1, chop_iterative(0, [1, 3, 5]))
        self.assertEqual(-1, chop_iterative(2, [1, 3, 5]))
        self.assertEqual(-1, chop_iterative(4, [1, 3, 5]))
        self.assertEqual(-1, chop_iterative(6, [1, 3, 5]))
    
    def test_four_items(self):
        self.assertEqual(0,  chop_iterative(1, [1, 3, 5, 7]))
        self.assertEqual(1,  chop_iterative(3, [1, 3, 5, 7]))
        self.assertEqual(2,  chop_iterative(5, [1, 3, 5, 7]))
        self.assertEqual(3,  chop_iterative(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_iterative(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_iterative(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_iterative(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_iterative(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_iterative(8, [1, 3, 5, 7]))

if __name__ == "__main__":
    unittest.main()