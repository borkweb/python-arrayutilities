import unittest
from arrayutilities import Arr

class TestArr(unittest.TestCase):
    def test_add_new_key(self):
        test_dict = {'a': 1}
        result = Arr.add(test_dict, 'b', 2)
        self.assertEqual(result, {'a': 1, 'b': 2}, "Should add a new key-value pair")

    def test_add_existing_key(self):
        test_dict = {'a': 1}
        result = Arr.add(test_dict, 'a', 3)
        self.assertEqual(result, {'a': 1}, "Should not modify existing key")

    def test_add_with_non_dict(self):
        test_list = [1, 2, 3]
        result = Arr.add(test_list, 1, 4)
        self.assertEqual(result, [1, 2, 3], "Should return the original list unmodified")

    def test_add_none_value(self):
        test_dict = {'a': 1}
        result = Arr.add(test_dict, 'b', None)
        self.assertEqual(result, {'a': 1, 'b': None}, "Should add key with None as value")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
