from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_merge_recursive_overlap_keys(self):
        array1 = {'a': 1, 'b': 2}
        array2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        result = Arr.merge_recursive(array1, array2)
        self.assertEqual(result, expected, "Should merge dictionaries with overlapping keys")

    def test_merge_recursive_one_empty_dict(self):
        array1 = {'a': 1}
        array2 = {}
        expected = {'a': 1}
        result = Arr.merge_recursive(array1, array2)
        self.assertEqual(result, expected, "Should return the non-empty dictionary when one dictionary is empty")

    def test_merge_recursive_both_empty_dicts(self):
        array1 = {}
        array2 = {}
        expected = {}
        result = Arr.merge_recursive(array1, array2)
        self.assertEqual(result, expected, "Should return an empty dictionary when both dictionaries are empty")

    def test_merge_recursive_nested_dicts(self):
        array1 = {'a': {'b': 1, 'c': 2}}
        array2 = {'a': {'d': 3}}
        expected = {'a': {'b': 1, 'c': 2, 'd': 3}}
        result = Arr.merge_recursive(array1, array2)
        self.assertEqual(result, expected, "Should merge dictionaries with nested dictionaries")

    def test_merge_recursive_nested_overlap_keys(self):
        array1 = {'a': {'b': 1, 'c': 2}}
        array2 = {'a': {'c': 3, 'd': 4}}
        expected = {'a': {'b': 1, 'c': 3, 'd': 4}}
        result = Arr.merge_recursive(array1, array2)
        self.assertEqual(result, expected, "Should merge dictionaries with nested dictionaries and overlapping keys")

if __name__ == '__main__':
    unittest.main()
