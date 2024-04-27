import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_key_exists(self):
        test_dict = {'a': 1, '1.5': 'exists'}
        self.assertTrue(Arr.exists(test_dict, 'a'), "Should return True if the key exists")

    def test_key_does_not_exist(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertFalse(Arr.exists(test_dict, 'c'), "Should return False if the key does not exist")

    def test_float_key_converted_and_exists(self):
        test_dict = {'1.5': 'exists'}
        self.assertTrue(Arr.exists(test_dict, 1.5), "Should return True if the float key exists when converted to string")

    def test_float_key_converted_and_does_not_exist(self):
        test_dict = {'1.5': 'exists'}
        self.assertFalse(Arr.exists(test_dict, 2.5), "Should return False if the float key does not exist even after conversion to string")

    def test_numeric_string_key(self):
        test_dict = {'1.5': 'exists', '2': 'also exists'}
        self.assertTrue(Arr.exists(test_dict, '1.5'), "Should return True for string keys that match numbers")

    def test_integer_key_in_string_form(self):
        test_dict = {'1': 'exists'}
        self.assertTrue(Arr.exists(test_dict, '1'), "Should handle string keys that are numeric")

    def test_integer_key_as_integer(self):
        test_dict = {1: 'exists'}
        self.assertTrue(Arr.exists(test_dict, 1), "Should return True for integer keys used as integers")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
