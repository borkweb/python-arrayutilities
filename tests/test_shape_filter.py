from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_shape_filter_simple_dict(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        shape = {'a': None, 'b': None}
        expected = {'a': 1, 'b': 2}
        result = Arr.shape_filter(test_dict, shape)
        self.assertEqual(result, expected, "Should filter the dictionary based on the provided shape")

    def test_shape_filter_nested_dict(self):
        test_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
        shape = {'a': {'b': None}}
        expected = {'a': {'b': 1}}
        result = Arr.shape_filter(test_dict, shape)
        self.assertEqual(result, expected, "Should filter nested dictionaries based on the provided shape")

    def test_shape_filter_missing_keys(self):
        test_dict = {'a': 1, 'b': 2}
        shape = {'a': None, 'c': None}
        expected = {'a': 1}
        result = Arr.shape_filter(test_dict, shape)
        self.assertEqual(result, expected, "Should filter only existing keys based on the provided shape")

if __name__ == '__main__':
    unittest.main()
