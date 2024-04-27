from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_has_single_key_exists(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertTrue(Arr.has(test_dict, 'a'), "Should return True if the key exists")

    def test_has_single_key_does_not_exist(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertFalse(Arr.has(test_dict, 'c'), "Should return False if the key does not exist")

    def test_has_multiple_keys_all_exist(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertTrue(Arr.has(test_dict, ['a', 'b']), "Should return True if all specified keys exist")

    def test_has_multiple_keys_some_exist(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertFalse(Arr.has(test_dict, ['a', 'c']), "Should return False if not all specified keys exist")

    def test_has_no_keys_specified(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertTrue(Arr.has(test_dict, []), "Should return True when no keys are specified")

    def test_has_empty_dict_no_keys_specified(self):
        test_dict = {}
        self.assertTrue(Arr.has(test_dict, []), "Should return True when no keys are specified and dictionary is empty")

    def test_has_empty_dict_keys_specified(self):
        test_dict = {}
        self.assertFalse(Arr.has(test_dict, ['a']), "Should return False when keys are specified and dictionary is empty")

if __name__ == '__main__':
    unittest.main()
