import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_empty_array(self):
        result = Arr.collapse([])
        self.assertEqual(result, [], "Should return an empty list when the input is an empty list")

    def test_flat_list(self):
        result = Arr.collapse([[1, 2, 3]])
        self.assertEqual(result, [1, 2, 3], "Should return the same list if nested inside another list")

    def test_nested_lists(self):
        result = Arr.collapse([[1, 2], [3, 4], [5]])
        self.assertEqual(result, [1, 2, 3, 4, 5], "Should flatten a list of lists into a single list")

    def test_mixed_elements(self):
        result = Arr.collapse([[1, 'a'], [3.5, 4], [True, None]])
        self.assertEqual(result, [1, 'a', 3.5, 4, True, None], "Should handle mixed types within nested lists")

    def test_nested_empty_lists(self):
        result = Arr.collapse([[], [1, 2], [], [3, 4], []])
        self.assertEqual(result, [1, 2, 3, 4], "Should handle nested empty lists without adding anything to the result")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
