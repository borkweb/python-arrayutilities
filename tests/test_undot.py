from arrayutilities import Arr
import unittest

class TestArrUndot(unittest.TestCase):
    def test_undot_with_flat_dictionary(self):
        array = {'a': 1, 'b': 2, 'c': 3}
        result = Arr.undot(array)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3}, "Should return the same dictionary for flat input")

    def test_undot_with_nested_dictionary(self):
        array = {'a.b': 1, 'a.c.d': 2, 'e.f.g': 3}
        result = Arr.undot(array)
        expected = {'a': {'b': 1, 'c': {'d': 2}}, 'e': {'f': {'g': 3}}}
        self.assertEqual(result, expected, "Should convert dotted keys to nested dictionaries")

    def test_undot_with_empty_dictionary(self):
        array = {}
        result = Arr.undot(array)
        self.assertEqual(result, {}, "Should return empty dictionary for empty input")

    def test_undot_with_nested_dictionary_and_duplicate_keys(self):
        array = {'a.b': 1, 'a.b.c': 2, 'a.b.c.d': 3}
        result = Arr.undot(array)
        expected = {'a': {'b': {'c': {'d': 3}}}}
        self.assertEqual(result, expected, "Should handle duplicate keys correctly")

    def test_undot_with_complex_dictionary(self):
        array = {'a.b': {'c.d': 1, 'e.f': 2}, 'g': {'h.i': 3}}
        result = Arr.undot(array)
        expected = {'a': {'b': {'c': {'d': 1}, 'e': {'f': 2}}}, 'g': {'h': {'i': 3}}}
        self.assertEqual(result, expected, "Should handle complex nested dictionaries")

if __name__ == '__main__':
    unittest.main()
