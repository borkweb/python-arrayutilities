from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_first_without_callback(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.first(test_dict)
        self.assertEqual(result, 1, "Should return the first element of the dictionary")

    def test_first_with_callback_match(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.first(test_dict, callback=lambda v, k: k == 'b')
        self.assertEqual(result, 2, "Should return the first element that matches the callback")

    def test_first_with_callback_no_match(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.first(test_dict, callback=lambda v, k: k == 'd', default='No Match')
        self.assertEqual(result, 'No Match', "Should return the default value when no element matches the callback")

    def test_first_empty_dictionary(self):
        test_dict = {}
        result = Arr.first(test_dict, default='Empty')
        self.assertEqual(result, 'Empty', "Should return the default value when the dictionary is empty")

    def test_first_with_none_default(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.first(test_dict, callback=lambda v, k: k == 'z', default=None)
        self.assertIsNone(result, "Should return None when no element matches and default is None")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
