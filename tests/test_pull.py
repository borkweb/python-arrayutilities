from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_pull_existing_key(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        key = 'b'
        expected_value = 2
        expected_array = {'a': 1, 'c': 3}
        result = Arr.pull(array, key)
        self.assertEqual(result, expected_value, "Should return the value associated with the specified key")
        self.assertEqual(array, expected_array, "Should remove the key-value pair from the array")

    def test_pull_nonexistent_key_with_default(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        key = 'd'
        default = 'not found'
        expected_value = 'not found'
        expected_array = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.pull(array, key, default)
        self.assertEqual(result, expected_value, "Should return the default value when the key does not exist")
        self.assertEqual(array, expected_array, "Should not modify the array when the key does not exist")

    def test_pull_nonexistent_key_without_default(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        key = 'd'
        expected_value = None
        expected_array = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.pull(array, key)
        self.assertEqual(result, expected_value, "Should return None when the key does not exist")
        self.assertEqual(array, expected_array, "Should not modify the array when the key does not exist")

if __name__ == '__main__':
    unittest.main()
