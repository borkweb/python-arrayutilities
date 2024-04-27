from arrayutilities import Arr
import unittest

class TestArrWhereNotNone(unittest.TestCase):
    def test_where_not_none_with_none_values(self):
        array = {'a': 1, 'b': None, 'c': 3, 'd': None}
        result = Arr.where_not_none(array)
        expected = {'a': 1, 'c': 3}
        self.assertEqual(result, expected, "Should return a dictionary without None values")

    def test_where_not_none_with_all_none_values(self):
        array = {'a': None, 'b': None, 'c': None}
        result = Arr.where_not_none(array)
        expected = {}
        self.assertEqual(result, expected, "Should return an empty dictionary when all values are None")

    def test_where_not_none_with_no_none_values(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.where_not_none(array)
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(result, expected, "Should return the original dictionary when there are no None values")

if __name__ == '__main__':
    unittest.main()
