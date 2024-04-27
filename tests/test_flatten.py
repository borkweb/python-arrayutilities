from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_flatten_no_nesting(self):
        test_array = [1, 2, 3]
        result = Arr.flatten(test_array)
        self.assertEqual(result, [1, 2, 3], "Should return the array unchanged when there is no nesting")

    def test_flatten_single_level_nesting(self):
        test_array = [1, [2, 3], 4]
        result = Arr.flatten(test_array)
        self.assertEqual(result, [1, 2, 3, 4], "Should flatten a single level nested array correctly")

    def test_flatten_multi_level_nesting(self):
        test_array = [1, [2, [3, 4]], 5]
        result = Arr.flatten(test_array)
        self.assertEqual(result, [1, 2, 3, 4, 5], "Should flatten a multi-level nested array correctly")

    def test_flatten_with_depth(self):
        test_array = [1, [2, [3, [4, 5]]], 6]
        result = Arr.flatten(test_array, depth=2)
        self.assertEqual(result, [1, 2, 3, [4, 5], 6], "Should flatten the array to the specified depth")

    def test_flatten_with_depth_one(self):
        test_array = [1, [2, [3, 4]], 5]
        result = Arr.flatten(test_array, depth=1)
        self.assertEqual(result, [1, 2, [3, 4], 5], "Should not flatten the array when depth is 1")

    def test_flatten_with_zero_depth(self):
        test_array = [1, [2, [3, 4]], 5]
        result = Arr.flatten(test_array, depth=0)
        self.assertEqual(result, [1, [2, [3, 4]], 5], "Should return the array unchanged when depth is 0")

    def test_flatten_empty_array(self):
        test_array = []
        result = Arr.flatten(test_array)
        self.assertEqual(result, [], "Should return an empty array when input is empty")

    def test_flatten_with_non_list_items(self):
        test_array = [1, "string", [2, "nested string"], 3]
        result = Arr.flatten(test_array)
        self.assertEqual(result, [1, "string", 2, "nested string", 3], "Should handle non-list items and flatten correctly")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
