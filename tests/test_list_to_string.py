from arrayutilities import Arr
import unittest

class TestArrToList(unittest.TestCase):
    def test_to_list_with_list_input(self):
        list_items = ['apple', 'banana', 'cherry']
        result = Arr.list_to_string(list_items)
        self.assertEqual(result, 'apple,banana,cherry', "Should join list items with comma by default")

    def test_to_list_with_list_input_and_custom_sep(self):
        list_items = ['apple', 'banana', 'cherry']
        result = Arr.list_to_string(list_items, sep=';')
        self.assertEqual(result, 'apple;banana;cherry', "Should join list items with custom separator")

    def test_to_list_with_string_input(self):
        list_items = 'apple, banana, cherry'
        result = Arr.list_to_string(list_items)
        self.assertEqual(result, 'apple, banana, cherry', "Should return the input string as is")

    def test_to_list_with_empty_input(self):
        list_items = ''
        result = Arr.list_to_string(list_items)
        self.assertEqual(result, '', "Should return empty string for empty input")

    def test_to_list_with_none_input(self):
        list_items = None
        result = Arr.list_to_string(list_items)
        self.assertIsNone(result, "Should return None for None input")

if __name__ == '__main__':
    unittest.main()
