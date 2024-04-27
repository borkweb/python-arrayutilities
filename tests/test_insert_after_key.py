from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_insert_after_key_exists(self):
        result = Arr.insert_after_key(2, [1, 2, 3, 4], 5)
        self.assertEqual(result, [1, 2, 5, 3, 4], "Should insert 5 after 2")

    def test_insert_after_key_does_not_exist(self):
        result = Arr.insert_after_key(9, [1, 2, 3, 4], 5)
        self.assertEqual(result, [1, 2, 3, 4, 5], "Should insert 5 at the end if 9 does not exist")

    def test_insert_after_key_with_list_insertion(self):
        result = Arr.insert_after_key(3, [1, 2, 3, 4], [5, 6])
        self.assertEqual(result, [1, 2, 3, 5, 6, 4], "Should insert list [5, 6] after 3")

    def test_insert_after_key_with_multiple_occurrences(self):
        result = Arr.insert_after_key(2, [1, 2, 3, 2, 4], 5)
        self.assertEqual(result, [1, 2, 5, 3, 2, 4], "Should insert after the first occurrence of 2")

    def test_insert_after_last_key(self):
        result = Arr.insert_after_key(4, [1, 2, 3, 4], 5)
        self.assertEqual(result, [1, 2, 3, 4, 5], "Should insert 5 after the last element 4")

    def test_insert_non_list_item(self):
        result = Arr.insert_after_key(3, [1, 2, 3, 4], 'a')
        self.assertEqual(result, [1, 2, 3, 'a', 4], "Should handle non-list item 'a' by inserting it correctly")

if __name__ == '__main__':
    unittest.main()
