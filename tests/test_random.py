from arrayutilities import Arr
import unittest
import random
from collections.abc import Mapping

class TestArr(unittest.TestCase):
    def setUp(self):
        self.test_array = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    def test_random_without_number(self):
        result = Arr.random(self.test_array)
        self.assertIn(result, self.test_array.values(), "Should return a random value from the array")

    def test_random_with_number(self):
        number = 3
        result = Arr.random(self.test_array, number=number)
        self.assertEqual(len(result), number, f"Should return {number} random elements from the array")

    def test_random_with_number_and_preserve_keys(self):
        number = 3
        result = Arr.random(self.test_array, number=number, preserve_keys=True)
        self.assertIsInstance(result, Mapping, "Should return a dictionary when preserve_keys is True")
        self.assertEqual(len(result), number, f"Should return {number} random elements with preserved keys")

    def test_random_with_zero_number(self):
        number = 0
        result = Arr.random(self.test_array, number=number)
        self.assertEqual(result, [], "Should return an empty list when number is 0")

    def test_random_with_large_number(self):
        number = len(self.test_array) + 1
        with self.assertRaises(ValueError):
            Arr.random(self.test_array, number=number)

if __name__ == '__main__':
    unittest.main()
