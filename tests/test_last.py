from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_last_no_callback_no_default(self):
        result = Arr.last([1, 2, 3])
        self.assertEqual(result, 3, "Should return the last element when no callback or default value is provided")

    def test_last_no_callback_with_default(self):
        result = Arr.last([])
        self.assertIsNone(result, "Should return None for an empty array with no default value")

    def test_last_no_callback_empty_array(self):
        result = Arr.last([], default='default')
        self.assertEqual(result, 'default', "Should return the default value for an empty array with a default value specified")

    def test_last_with_callback(self):
        result = Arr.last([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        self.assertEqual(result, 4, "Should return the last even element when a callback is provided")

    def test_last_with_callback_no_match(self):
        result = Arr.last([1, 3, 5], lambda x: x % 2 == 0, default='no match')
        self.assertEqual(result, 'no match', "Should return the default value when no element matches the callback condition")

    def test_last_with_callback_empty_array(self):
        result = Arr.last([], lambda x: x % 2 == 0, default='no match')
        self.assertEqual(result, 'no match', "Should return the default value for an empty array when a callback is provided")

    def test_last_with_callback_no_default(self):
        result = Arr.last([], lambda x: x % 2 == 0)
        self.assertIsNone(result, "Should return None when no match is found and no default value is provided")

if __name__ == '__main__':
    unittest.main()
