from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_list_insertion(self):
        result = Arr.insert_before_key(1, [10, 20, 30], 25)
        self.assertEqual(result, [10, 25, 20, 30])

    def test_list_insertion_out_of_bounds(self):
        with self.assertRaises(IndexError):
            Arr.insert_before_key(4, [10, 20, 30], 40)

    def test_dict_insertion_existing_key(self):
        result = Arr.insert_before_key('b', {'a': 1, 'b': 2, 'c': 3}, {'new': 25})
        expected = {'a': 1, 'new': 25, 'b': 2, 'c': 3}
        self.assertEqual(result, expected)

    def test_dict_insertion_non_existing_key(self):
        with self.assertRaises(KeyError):
            Arr.insert_before_key('x', {'a': 1, 'b': 2, 'c': 3}, {'x': 25})

    def test_dict_insertion_non_dict_insert(self):
        with self.assertRaises(TypeError):
            Arr.insert_before_key('b', {'a': 1, 'b': 2, 'c': 3}, 25)

    def test_insert_non_list_non_dict(self):
        with self.assertRaises(TypeError):
            Arr.insert_before_key(1, 'not a list or dict', 'hello')

if __name__ == '__main__':
    unittest.main()
