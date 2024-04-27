from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_only_with_existing_keys(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        keys = ['a', 'c']
        expected = {'a': 1, 'c': 3}
        result = Arr.only(array, keys)
        self.assertEqual(result, expected, "Should return a dictionary with only the specified keys")

    def test_only_with_nonexistent_keys(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        keys = ['x', 'y', 'z']
        expected = {}
        result = Arr.only(array, keys)
        self.assertEqual(result, expected, "Should return an empty dictionary if none of the keys exist in the array")

    def test_only_with_empty_keys(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        keys = []
        expected = {}
        result = Arr.only(array, keys)
        self.assertEqual(result, expected, "Should return an empty dictionary if no keys are provided")

    def test_only_with_empty_array(self):
        array = {}
        keys = ['a', 'b', 'c']
        expected = {}
        result = Arr.only(array, keys)
        self.assertEqual(result, expected, "Should return an empty dictionary if the array is empty")

    def test_only_with_mixed_keys(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        keys = ['a', 'x', 'c']
        expected = {'a': 1, 'c': 3}
        result = Arr.only(array, keys)
        self.assertEqual(result, expected, "Should return a dictionary with only the existing keys")

if __name__ == '__main__':
    unittest.main()
