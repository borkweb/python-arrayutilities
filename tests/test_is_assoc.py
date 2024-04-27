from arrayutils import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_is_assoc_with_dict(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertTrue(Arr.is_assoc(test_dict), "Should return True for dictionaries")

    def test_is_assoc_with_list(self):
        test_list = [1, 2, 3]
        self.assertFalse(Arr.is_assoc(test_list), "Should return False for lists")

    def test_is_assoc_with_empty_dict(self):
        test_dict = {}
        self.assertTrue(Arr.is_assoc(test_dict), "Should return True for empty dictionaries")

    def test_is_assoc_with_empty_list(self):
        test_list = []
        self.assertFalse(Arr.is_assoc(test_list), "Should return False for empty lists")

    def test_is_assoc_with_string(self):
        test_string = "hello"
        self.assertFalse(Arr.is_assoc(test_string), "Should return False for non-list types like strings")

    def test_is_assoc_with_integer(self):
        test_integer = 100
        self.assertFalse(Arr.is_assoc(test_integer), "Should return False for non-list types like integers")

    def test_is_assoc_with_tuple(self):
        test_tuple = (1, 2, 3)
        self.assertFalse(Arr.is_assoc(test_tuple), "Should return False for tuple, as it's not a list")

if __name__ == '__main__':
    unittest.main()
