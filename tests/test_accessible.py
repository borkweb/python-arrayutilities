import unittest
from arrayutilities import Arr
from collections import UserDict

class TestArr(unittest.TestCase):
    def test_accessible_with_list(self):
        self.assertTrue(Arr.accessible([]), "Should be True for lists")

    def test_accessible_with_dict(self):
        self.assertTrue(Arr.accessible({}), "Should be True for dicts")

    def test_accessible_with_userdict(self):
        self.assertTrue(Arr.accessible(UserDict()), "Should be True for UserDict")

    def test_accessible_with_int(self):
        self.assertFalse(Arr.accessible(123), "Should be False for integers")

    def test_accessible_with_string(self):
        self.assertFalse(Arr.accessible("hello"), "Should be False for strings")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
