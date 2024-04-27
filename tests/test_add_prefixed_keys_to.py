import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_add_prefixed_keys_non_dict(self):
        result = Arr.add_prefixed_keys_to([1, 2, 3])
        self.assertEqual(result, [1, 2, 3], "Should return the original list unmodified")

    def test_add_prefixed_keys_simple_dict(self):
        test_dict = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2, '_a': 1, '_b': 2}
        result = Arr.add_prefixed_keys_to(test_dict)
        self.assertEqual(result, expected, "Should add prefixed keys to dictionary")

    def test_add_prefixed_keys_with_existing_prefix(self):
        test_dict = {'_a': 1, 'b': 2}
        expected = {'_a': 1, 'b': 2, '_b': 2}
        result = Arr.add_prefixed_keys_to(test_dict)
        self.assertEqual(result, expected, "Should add prefixes without affecting already prefixed keys")

    def test_add_prefixed_keys_recursive(self):
        test_dict = {'a': {'c': 3}, 'b': 2}
        expected = {'a': {'c': 3, '_c': 3}, 'b': 2, '_a': {'c': 3, '_c': 3}, '_b': 2}
        result = Arr.add_prefixed_keys_to(test_dict, recursive=True)
        self.assertEqual(result, expected, "Should add prefixed keys recursively to nested dictionaries")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
