from arrayutilities import Arr
import unittest

class TestListToDict(unittest.TestCase):

    def test_with_list(self):
        # Test with a simple list
        input_list = ['apple', 'banana', 'cherry']
        expected_dict = {0: 'apple', 1: 'banana', 2: 'cherry'}
        result = Arr.list_to_dict(input_list)
        self.assertEqual(result, expected_dict)

    def test_with_empty_list(self):
        # Test with an empty list
        input_list = []
        expected_dict = {}
        result = Arr.list_to_dict(input_list)
        self.assertEqual(result, expected_dict)

    def test_with_dict(self):
        # Test with a dict input, should return the dict unchanged
        input_dict = {'a': 1, 'b': 2}
        result = Arr.list_to_dict(input_dict)
        self.assertEqual(result, input_dict)

    def test_with_non_list(self):
        # Test with a non-list and non-dict input, should handle or raise an error
        input_value = 'not a list'
        result = Arr.list_to_dict(input_value)
        self.assertEqual(result, {0: 'not a list'})

# Running the tests
if __name__ == '__main__':
    unittest.main()
