from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_list_insertion(self):
        # Tests insertion into a list when the key is an index
        result = Arr.insert_after_key(1, [10, 20, 30], 25)
        self.assertEqual(result, [10, 20, 25, 30])

    def test_list_insertion_out_of_bounds(self):
        # Tests insertion at the end if the index is out of range
        result = Arr.insert_after_key(5, [10, 20, 30], 40)
        self.assertEqual(result, [10, 20, 30, 40])

    def test_dict_insertion_existing_key(self):
        # Tests insertion into a dictionary when the key exists
        result = Arr.insert_after_key('b', {'a': 1, 'b': 2, 'c': 3}, {'new': 25})
        expected = {'a': 1, 'b': 2, 'new': 25, 'c': 3}
        self.assertEqual(result, expected)

    def test_dict_insertion_non_existing_key(self):
        # Tests insertion at the end if the key does not exist
        result = Arr.insert_after_key('x', {'a': 1, 'b': 2, 'c': 3}, {'x': 25})
        expected = {'a': 1, 'b': 2, 'c': 3, 'x': 25}
        self.assertEqual(result, expected)

    def test_dict_insertion_non_dict_insert(self):
        # Tests non-dict insert in a dict (should ideally raise an error or follow specific logic)
        with self.assertRaises(TypeError):
            Arr.insert_after_key('b', {'a': 1, 'b': 2, 'c': 3}, 25)

    def test_insert_non_list_non_dict(self):
        # Tests handling of non-list and non-dict source
        with self.assertRaises(TypeError):
            Arr.insert_after_key(1, 'not a list or dict', 'hello')

if __name__ == '__main__':
    unittest.main()
