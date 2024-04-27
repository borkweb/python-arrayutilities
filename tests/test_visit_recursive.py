import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_non_dict_input(self):
        result = Arr.visit_recursive([1, 2, 3], lambda k, v: (k, v))
        self.assertEqual(result, [1, 2, 3], "Should return non-dict input as is")

    def test_simple_dict(self):
        test_dict = {'a': 1, 'b': 2}
        result = Arr.visit_recursive(test_dict, lambda k, v: (k, v * 2))
        expected = {'a': 2, 'b': 4}
        self.assertEqual(result, expected, "Should process simple dictionary and apply visitor to values")

    def test_recursive_dict(self):
        test_dict = {'a': {'c': 3}, 'b': 2}
        result = Arr.visit_recursive(test_dict, lambda k, v: (k, v if isinstance(v, dict) else v * 3))
        expected = {'a': {'c': 9}, 'b': 6}
        self.assertEqual(result, expected, "Should process nested dictionary recursively")

    def test_ignore_none_keys(self):
        test_dict = {'a': 1, 'b': 2}
        result = Arr.visit_recursive(test_dict, lambda k, v: (None, v * 2) if k == 'a' else (k, v * 2))
        expected = {'b': 4}
        self.assertEqual(result, expected, "Should exclude keys where visitor returns None for key")

    def test_key_modification(self):
        test_dict = {'a': 1, 'b': 2}
        result = Arr.visit_recursive(test_dict, lambda k, v: (k.upper(), v))
        expected = {'A': 1, 'B': 2}
        self.assertEqual(result, expected, "Should modify keys based on visitor output")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
