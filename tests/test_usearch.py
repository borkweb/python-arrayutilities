from arrayutilities import Arr
import unittest

class TestArrUsearch(unittest.TestCase):
    def test_usearch_with_existing_value(self):
        def callback(needle, value, key):
            return needle == value

        haystack = {'a': 1, 'b': 2, 'c': 3}
        needle = 2

        result = Arr.usearch(needle, haystack, callback)
        self.assertEqual(result, 'b', "Should return the key of the first occurrence of the value")

    def test_usearch_with_non_existing_value(self):
        def callback(needle, value, key):
            return needle == value

        haystack = {'a': 1, 'b': 2, 'c': 3}
        needle = 5

        result = Arr.usearch(needle, haystack, callback)
        self.assertFalse(result, "Should return False if value is not found")

    def test_usearch_with_custom_callback(self):
        def custom_callback(needle, value, key):
            return needle in key

        haystack = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
        needle = 'an'

        result = Arr.usearch(needle, haystack, custom_callback)
        self.assertEqual(result, 'banana', "Should return the key where the custom callback returns True")

if __name__ == "__main__":
    unittest.main()
