from arrayutilities import Arr
import unittest
import time

class TestStringifyKeys(unittest.TestCase):
    def test_stringify_keys_with_prefix(self):
        test_array = {'a': 1, 'b': 2, 'c': 3}
        prefix = 'prefix_'
        result = Arr.stringify_keys(test_array, prefix)
        expected = {'prefix_a': 1, 'prefix_b': 2, 'prefix_c': 3}
        self.assertEqual(result, expected, "Should add the prefix to all keys")

    def test_stringify_keys_without_prefix(self):
        test_array = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.stringify_keys(test_array)
        expected = {f'a': 1, f'b': 2, f'c': 3}
        self.assertEqual(result, expected, "Should add a default prefix to all keys if no prefix is provided")

    def test_stringify_keys_with_integer_keys(self):
        test_array = {1: 'a', 2: 'b', 3: 'c'}
        result = Arr.stringify_keys(test_array, 'sk_')
        expected = {f'sk_1': 'a', f'sk_2': 'b', f'sk_3': 'c'}
        self.assertEqual(result, expected, "Should handle integer keys correctly")

if __name__ == '__main__':
    unittest.main()
