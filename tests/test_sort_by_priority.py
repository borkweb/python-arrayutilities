from arrayutilities import Arr
import unittest

class TestSortByPriority(unittest.TestCase):
    def test_sort_by_priority_empty_array(self):
        input_array = []
        expected_result = []
        result = Arr.sort_by_priority(input_array)
        self.assertEqual(result, expected_result, "Should return an empty array for an empty input array")

    def test_sort_by_priority_single_element(self):
        input_array = [{'priority': 2}]
        expected_result = [{'priority': 2}]
        result = Arr.sort_by_priority(input_array)
        self.assertEqual(result, expected_result, "Should return the same array for a single element array")

    def test_sort_by_priority_no_priority_key(self):
        input_array = [{'name': 'John'}, {'age': 25}]
        expected_result = [{'name': 'John'}, {'age': 25}]
        result = Arr.sort_by_priority(input_array)
        self.assertEqual(result, expected_result, "Should return the same array when priority key is missing")

    def test_sort_by_priority_multiple_elements(self):
        input_array = [{'name': 'John', 'priority': 2}, {'name': 'Alice', 'priority': 1}, {'name': 'Bob', 'priority': 3}]
        expected_result = [{'name': 'Alice', 'priority': 1}, {'name': 'John', 'priority': 2}, {'name': 'Bob', 'priority': 3}]
        result = Arr.sort_by_priority(input_array)
        self.assertEqual(result, expected_result, "Should sort the array based on priority")

if __name__ == '__main__':
    unittest.main()
