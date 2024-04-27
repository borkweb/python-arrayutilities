from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_prepend_to_list(self):
        array = [2, 3, 4]
        value = 1
        expected = [1, 2, 3, 4]
        result = Arr.prepend(array, value)
        self.assertEqual(result, expected, "Should prepend a value to a list")

    def test_prepend_to_dict_without_key(self):
        array = {'b': 2, 'c': 3}
        value = 1
        expected = {0: 1, 'b': 2, 'c': 3}
        result = Arr.prepend(array, value)
        self.assertEqual(result, expected, "Should prepend a value to a dictionary without specifying a key")

    def test_prepend_to_dict_with_key(self):
        array = {'b': 2, 'c': 3}
        value = 1
        key = 'a'
        expected = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.prepend(array, value, key)
        self.assertEqual(result, expected, "Should prepend a value to a dictionary with a specified key")

    def test_prepend_to_empty_list(self):
        array = []
        value = 1
        expected = [1]
        result = Arr.prepend(array, value)
        self.assertEqual(result, expected, "Should prepend a value to an empty list")

    def test_prepend_to_empty_dict(self):
        array = {}
        value = 1
        expected = {0: 1}
        result = Arr.prepend(array, value)
        self.assertEqual(result, expected, "Should prepend a value to an empty dictionary")

if __name__ == '__main__':
    unittest.main()
