import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_add_unprefixed_keys_non_dict(self):
        result = Arr.add_unprefixed_keys_to([1, 2, 3])
        self.assertEqual(result, [1, 2, 3], "Should return the original list unmodified")

    def test_add_unprefixed_keys_simple_dict(self):
        test_dict = {'_a': 1, '_b': 2}
        expected = {'_a': 1, '_b': 2, 'a': 1, 'b': 2}
        result = Arr.add_unprefixed_keys_to(test_dict)
        self.assertEqual(result, expected, "Should add unprefixed keys to dictionary")

    def test_add_unprefixed_keys_with_non_prefixed_keys(self):
        test_dict = {'_a': 1, 'b': 2}
        expected = {'_a': 1, 'b': 2, 'a': 1}
        result = Arr.add_unprefixed_keys_to(test_dict)
        self.assertEqual(result, expected, "Should add unprefixed versions of prefixed keys only")

    def test_add_unprefixed_keys_recursive(self):
        test_dict = {'_a': {'_c': 3}, 'b': 2}
        expected = {'_a': {'_c': 3, 'c': 3}, 'b': 2, 'a': {'_c': 3, 'c': 3}}
        result = Arr.add_unprefixed_keys_to(test_dict, recursive=True)
        self.assertEqual(result, expected, "Should add unprefixed keys recursively to nested dictionaries")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
