from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_list_to_array_with_default_separator(self):
        result = Arr.list_to_array("apple, banana, cherry")
        self.assertEqual(result, ["apple", "banana", "cherry"], "Should convert string with default separator to list")

    def test_list_to_array_with_custom_separator(self):
        result = Arr.list_to_array("apple|banana|cherry", sep="|")
        self.assertEqual(result, ["apple", "banana", "cherry"], "Should convert string with custom separator to list")

    def test_list_to_array_empty_string(self):
        result = Arr.list_to_array("")
        self.assertEqual(result, [], "Should return an empty list for empty string")

    def test_list_to_array_with_empty_elements(self):
        result = Arr.list_to_array("apple,,banana,")
        self.assertEqual(result, ["apple", "banana"], "Should remove empty elements from string")

    def test_list_to_array_list_input(self):
        result = Arr.list_to_array(["apple", "banana", "cherry"])
        self.assertEqual(result, ["apple", "banana", "cherry"], "Should return the input list unchanged")

    def test_list_to_array_whitespace_elements(self):
        result = Arr.list_to_array(" apple , banana , cherry ")
        self.assertEqual(result, ["apple", "banana", "cherry"], "Should remove leading/trailing whitespace from elements")

    def test_list_to_array_whitespace_string(self):
        result = Arr.list_to_array("  ")
        self.assertEqual(result, [], "Should return an empty list for string with only whitespace")

if __name__ == '__main__':
    unittest.main()
