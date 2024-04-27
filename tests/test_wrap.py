from arrayutilities import Arr
import unittest

class TestArrWrap(unittest.TestCase):
    def test_wrap_with_none_value(self):
        result = Arr.wrap(None)
        expected = []
        self.assertEqual(result, expected, "Should return an empty list when the input is None")

    def test_wrap_with_single_value(self):
        result = Arr.wrap(5)
        expected = [5]
        self.assertEqual(result, expected, "Should wrap a single value in a list")

    def test_wrap_with_list_value(self):
        result = Arr.wrap([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(result, expected, "Should return the original list when input is a list")

    def test_wrap_with_string_value(self):
        result = Arr.wrap("hello")
        expected = ["hello"]
        self.assertEqual(result, expected, "Should wrap a string value in a list")

if __name__ == '__main__':
    unittest.main()
