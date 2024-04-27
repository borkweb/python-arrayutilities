from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_filter_by_prefix(self):
        test_dict = {'pref_one': 1, 'pref_two': 2, 'nopref_three': 3}
        result = Arr.filter_prefixed(test_dict, 'pref_')
        expected = {'pref_one': 1, 'pref_two': 2}
        self.assertEqual(result, expected, "Should return dictionary items that match the prefix")

    def test_filter_no_match(self):
        test_dict = {'one': 1, 'two': 2, 'three': 3}
        result = Arr.filter_prefixed(test_dict, 'pref_')
        self.assertEqual(result, {}, "Should return an empty dictionary when no keys match the prefix")

    def test_empty_dictionary(self):
        result = Arr.filter_prefixed({}, 'pref_')
        self.assertEqual(result, {}, "Should return an empty dictionary when input dictionary is empty")

    def test_filter_numeric_prefix(self):
        test_dict = {'123_one': 1, '123_two': 2, '234_three': 3}
        result = Arr.filter_prefixed(test_dict, '123_')
        expected = {'123_one': 1, '123_two': 2}
        self.assertEqual(result, expected, "Should return dictionary items that start with a numeric prefix")

    def test_filter_special_char_prefix(self):
        test_dict = {'@key1': 1, '@key2': 2, 'key3': 3}
        result = Arr.filter_prefixed(test_dict, '@')
        expected = {'@key1': 1, '@key2': 2}
        self.assertEqual(result, expected, "Should return dictionary items that start with a special character prefix")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
