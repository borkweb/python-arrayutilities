from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_recursive_ksort_simple_dict(self):
        test_dict = {'b': 2, 'a': 1}
        expected = {'a': 1, 'b': 2}
        result = Arr.recursive_ksort(test_dict)
        self.assertEqual(result, expected, "Should sort the keys of a simple dictionary alphabetically")

    def test_recursive_ksort_nested_dict(self):
        test_dict = {'b': {'d': 4, 'c': 3}, 'a': {'e': 5, 'f': 6}}
        expected = {'a': {'e': 5, 'f': 6}, 'b': {'c': 3, 'd': 4}}
        result = Arr.recursive_ksort(test_dict)
        self.assertEqual(result, expected, "Should sort the keys of nested dictionaries alphabetically")

    def test_recursive_ksort_mixed_data_types(self):
        test_dict = {'b': 2, 'a': {'c': 3, 'b': 2}, 'd': [4, 3, 2], 'c': 'hello'}
        expected = {'a': {'b': 2, 'c': 3}, 'b': 2, 'c': 'hello', 'd': [4, 3, 2]}
        result = Arr.recursive_ksort(test_dict)
        self.assertEqual(result, expected, "Should sort the keys of mixed data types alphabetically")

if __name__ == '__main__':
    unittest.main()
