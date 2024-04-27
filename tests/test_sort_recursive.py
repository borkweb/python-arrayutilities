from arrayutilities import Arr
import unittest

class TestSortRecursive(unittest.TestCase):
    def test_sort_recursive_empty_array(self):
        input_array = {}
        expected_result = {}
        result = Arr.sort_recursive(input_array)
        self.assertEqual(result, expected_result, "Should return an empty dictionary for an empty input dictionary")

    def test_sort_recursive_single_element(self):
        input_array = {'b': 2}
        expected_result = {'b': 2}
        result = Arr.sort_recursive(input_array)
        self.assertEqual(result, expected_result, "Should return the same dictionary for a single element dictionary")

    def test_sort_recursive_nested_elements(self):
        input_array = {'c': 3, 'a': {'b': 2, 'd': 4}}
        expected_result = {'a': {'b': 2, 'd': 4}, 'c': 3}
        result = Arr.sort_recursive(input_array)
        self.assertEqual(result, expected_result, "Should sort the dictionary recursively")

    def test_sort_recursive_nested_elements_descending(self):
        input_array = {'c': 3, 'a': {'b': 2, 'd': 4}}
        expected_result = {'c': 3, 'a': {'d': 4, 'b': 2}}
        result = Arr.sort_recursive(input_array, descending=True)
        self.assertEqual(result, expected_result, "Should sort the dictionary recursively in descending order")

if __name__ == '__main__':
    unittest.main()
