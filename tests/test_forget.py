from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_forget_flat_key(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        Arr.forget(test_dict, 'b')
        self.assertNotIn('b', test_dict, "Key 'b' should be removed from the dictionary")

    def test_forget_nested_key(self):
        test_dict = {'a': 1, 'b': {'c': 2, 'd': 3}}
        Arr.forget(test_dict, 'b.c')
        self.assertNotIn('c', test_dict['b'], "Nested key 'c' should be removed from dictionary under 'b'")

    def test_forget_non_existent_key(self):
        test_dict = {'a': 1, 'b': 2}
        Arr.forget(test_dict, 'c')
        self.assertIn('a', test_dict, "Existing keys should remain unchanged when non-existent key is specified")
        self.assertIn('b', test_dict, "Existing keys should remain unchanged when non-existent key is specified")

    def test_forget_multiple_keys(self):
        test_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
        Arr.forget(test_dict, ['a', 'c.d'])
        self.assertNotIn('a', test_dict, "Key 'a' should be removed")
        self.assertNotIn('d', test_dict['c'], "Nested key 'd' should be removed under 'c'")
        self.assertIn('e', test_dict['c'], "Key 'e' under 'c' should remain")

    def test_forget_empty_keys_list(self):
        test_dict = {'a': 1, 'b': 2}
        Arr.forget(test_dict, [])
        self.assertIn('a', test_dict, "Dictionary should remain unchanged when empty key list is provided")
        self.assertIn('b', test_dict, "Dictionary should remain unchanged when empty key list is provided")

if __name__ == '__main__':
    unittest.main()
