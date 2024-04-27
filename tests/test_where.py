from arrayutilities import Arr
import unittest

class TestArrWhere(unittest.TestCase):
    def test_where_with_even_numbers(self):
        def callback(value, key):
            return value % 2 == 0

        array = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

        result = Arr.where(array, callback)
        expected = {'b': 2, 'd': 4}
        self.assertEqual(result, expected, "Should return a dictionary with only even numbers")

    def test_where_with_longer_than_three_characters(self):
        def callback(value, key):
            return len(key) > 4

        array = {'apple': 1, 'banana': 2, 'grape': 3, 'kiwi': 4}

        result = Arr.where(array, callback)
        expected = {'apple': 1, 'banana': 2, 'grape': 3}
        self.assertEqual(result, expected, "Should return a dictionary with keys longer than three characters")

    def test_where_with_custom_callback(self):
        def custom_callback(value, key):
            return key.startswith('a') and value > 0

        array = {'apple': 1, 'banana': -2, 'grape': 3, 'kiwi': 0}

        result = Arr.where(array, custom_callback)
        expected = {'apple': 1}
        self.assertEqual(result, expected, "Should return a dictionary with keys starting with 'a' and positive values")

if __name__ == "__main__":
    unittest.main()
