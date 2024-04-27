from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_get_flat_key(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.get(test_dict, 'b')
        self.assertEqual(result, 2, "Should return the value of key 'b'")

    def test_get_nested_key(self):
        test_dict = {'a': 1, 'b': {'c': 2, 'd': 3}}
        result = Arr.get(test_dict, ['b', 'c'])
        self.assertEqual(result, 2, "Should return the value of nested key 'c' under 'b'")

    def test_get_deep_nested_key(self):
        test_dict = {'a': 1, 'b': {'c': { 'e': 2}, 'd': 3}}
        result = Arr.get(test_dict, ['b', 'c', 'e'])
        self.assertEqual(result, 2, "Should return the value of nested key 'e' under 'c' under 'b'")

        result = Arr.get(test_dict, ['b', 'd'])
        self.assertEqual(result, 3, "Should return the value of nested key 'd' under 'b'")

    def test_get_non_existent_key_returns_default(self):
        test_dict = {'a': 1, 'b': 2}
        result = Arr.get(test_dict, 'c', default='Not Found')
        self.assertEqual(result, 'Not Found', "Should return the default value when key does not exist")

    def test_get_nested_non_existent_key_returns_default(self):
        test_dict = {'a': {'b': 2}}
        result = Arr.get(test_dict, ['a', 'c'], default='Not Found')
        self.assertEqual(result, 'Not Found', "Should return the default value when nested key does not exist")

    def test_get_with_index_error_in_list(self):
        test_list = [1, 2, 3]
        result = Arr.get(test_list, 5, default='Out of Index')
        self.assertEqual(result, 'Out of Index', "Should return default when index is out of bounds")

    def test_get_with_type_error(self):
        test_mixed = {'a': 1, 'b': [2, 3]}
        result = Arr.get(test_mixed, ['b', 'x'], default='Type Error')
        self.assertEqual(result, 'Type Error', "Should return default on a type mismatch error (accessing list with string key)")

    def test_get_without_default(self):
        test_dict = {'a': 1, 'b': 2}
        result = Arr.get(test_dict, 'c')
        self.assertIsNone(result, "Should return None as default when no default is specified and key does not exist")

if __name__ == '__main__':
    unittest.main()
