from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_join_with_glue_only(self):
        result = Arr.join(['apple', 'banana', 'cherry'], ', ')
        self.assertEqual(result, 'apple, banana, cherry', "Should join items with only glue")

    def test_join_with_final_glue(self):
        result = Arr.join(['apple', 'banana', 'cherry'], ', ', ', and ')
        self.assertEqual(result, 'apple, banana, and cherry', "Should join items with a final glue before the last item")

    def test_join_single_item(self):
        result = Arr.join(['apple'], ', ', ', and ')
        self.assertEqual(result, 'apple', "Should handle single item lists without adding glue")

    def test_join_no_items(self):
        result = Arr.join([], ', ', ', and ')
        self.assertEqual(result, '', "Should return an empty string for empty list")

    def test_join_no_items_no_glues(self):
        result = Arr.join([], ', ')
        self.assertEqual(result, '', "Should return an empty string for empty list with only primary glue")

    def test_join_two_items_with_final_glue(self):
        result = Arr.join(['apple', 'banana'], ', ', ', and ')
        self.assertEqual(result, 'apple, and banana', "Should join two items using the final glue")

    def test_join_with_numeric_items(self):
        result = Arr.join([1, 2, 3], '-', '-')
        self.assertEqual(result, '1-2-3', "Should join numeric items, converting them to strings")

    def test_join_with_one_numeric_item(self):
        result = Arr.join([1], '-', '-')
        self.assertEqual(result, '1', "Should join numeric items, converting them to strings")
if __name__ == '__main__':
    unittest.main()
