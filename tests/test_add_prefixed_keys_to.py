import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_add_prefixed_keys_non_dict(self):
        test_list = [1, 2, 3]
        expected = {0: 1, 1: 2, 2: 3, '_0': 1, '_1': 2, '_2': 3}
        result = Arr.add_prefixed_keys_to([1, 2, 3])
        self.assertEqual(result, expected, "Should return a dict with prefixed keys added")

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

    def test_add_prefixed_keys_list(self):
        test_dict = [ 1, 2 ]
        expected = {0: 1, 1: 2, '_0': 1, '_1': 2}
        result = Arr.add_prefixed_keys_to(test_dict)
        self.assertEqual(result, expected, "Should add prefixed keys to dictionary")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
