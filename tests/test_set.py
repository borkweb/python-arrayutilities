from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_set_single_key(self):
        test_array = {}
        keys = 'a'
        value = 1
        expected = {'a': 1}
        result = Arr.set(test_array, keys, value)
        self.assertEqual(result, expected, "Should set a value for a single key")

    def test_set_nested_keys(self):
        test_array = {}
        keys = ['a', 'b', 'c']
        value = 1
        expected = {'a': {'b': {'c': 1}}}
        result = Arr.set(test_array, keys, value)
        self.assertEqual(result, expected, "Should set a value for nested keys")

    def test_set_existing_nested_keys(self):
        test_array = {'a': {'b': {'c': 1}}}
        keys = ['a', 'b', 'd']
        value = 2
        expected = {'a': {'b': {'c': 1, 'd': 2}}}
        result = Arr.set(test_array, keys, value)
        self.assertEqual(result, expected, "Should set a value for existing nested keys")

if __name__ == '__main__':
    unittest.main()
