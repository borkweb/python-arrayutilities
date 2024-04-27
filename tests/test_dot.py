import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_empty_dict(self):
        result = Arr.dot({})
        self.assertEqual(result, {}, "Should return an empty dictionary when the input is empty")

    def test_flat_dict(self):
        test_dict = {'a': 1, 'b': 2}
        result = Arr.dot(test_dict)
        self.assertEqual(result, {'a': 1, 'b': 2}, "Should handle flat dictionaries without modification")

    def test_nested_dict(self):
        test_dict = {'a': {'b': 2, 'c': 3}}
        result = Arr.dot(test_dict)
        self.assertEqual(result, {'a.b': 2, 'a.c': 3}, "Should correctly flatten a nested dictionary")

    def test_deeply_nested_dict(self):
        test_dict = {'a': {'b': {'c': {'d': 4}}}}
        result = Arr.dot(test_dict)
        self.assertEqual(result, {'a.b.c.d': 4}, "Should correctly flatten a deeply nested dictionary")

    def test_multiple_nested_levels(self):
        test_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
        result = Arr.dot(test_dict)
        expected = {'a': 1, 'b.c': 2, 'b.d.e': 3}
        self.assertEqual(result, expected, "Should handle dictionaries with multiple nested levels and flatten them correctly")

    def test_with_initial_prepend(self):
        test_dict = {'a': 1}
        result = Arr.dot(test_dict, 'init.')
        self.assertEqual(result, {'init.a': 1}, "Should correctly prepend a given string to the keys")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
