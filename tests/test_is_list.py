from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_is_list_with_list(self):
        self.assertTrue(Arr.is_list([1, 2, 3]), "Should return True for lists")

    def test_is_list_with_empty_list(self):
        self.assertTrue(Arr.is_list([]), "Should return True for an empty list")

    def test_is_list_with_dict(self):
        self.assertFalse(Arr.is_list({'a': 1, 'b': 2}), "Should return False for dictionaries")

    def test_is_list_with_string(self):
        self.assertFalse(Arr.is_list("hello"), "Should return False for strings")

    def test_is_list_with_integer(self):
        self.assertFalse(Arr.is_list(123), "Should return False for integers")

    def test_is_list_with_tuple(self):
        self.assertFalse(Arr.is_list((1, 2, 3)), "Should return False for tuples")

    def test_is_list_with_mixed_list(self):
        self.assertTrue(Arr.is_list([1, "a", None]), "Should return True for a list containing mixed data types")

if __name__ == '__main__':
    unittest.main()
