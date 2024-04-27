from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_query_with_dict(self):
        array = {'name': 'John', 'age': 30, 'city': 'New York'}
        expected_query = 'name=John&age=30&city=New+York'
        result = Arr.query(array)
        self.assertEqual(result, expected_query, "Should return the correct URL-encoded query string")

    def test_query_with_nested_dict(self):
        array = {'name': 'John', 'info': {'age': 30, 'city': 'New York'}}
        expected_query = 'name=John&info[age]=30&info[city]=New+York'
        result = Arr.query(array)
        self.assertEqual(result, expected_query, "Should handle nested dictionaries correctly")

    def test_query_with_deep_nested_dict(self):
        array = {'name': 'John', 'info': {'age': 30, 'city': ['New York', 'Phoenix']}}
        expected_query = 'name=John&info[age]=30&info[city][0]=New+York&info[city][1]=Phoenix'
        result = Arr.query(array)
        self.assertEqual(result, expected_query, "Should handle deep nested dictionaries correctly")

    def test_query_with_list(self):
        array = {'name': 'John', 'hobbies': ['reading', 'painting']}
        expected_query = 'name=John&hobbies[0]=reading&hobbies[1]=painting'
        result = Arr.query(array)
        self.assertEqual(result, expected_query, "Should handle lists correctly by repeating the key")

    def test_query_with_empty_dict(self):
        array = {}
        expected_query = ''
        result = Arr.query(array)
        self.assertEqual(result, expected_query, "Should return an empty string for an empty dictionary")

if __name__ == '__main__':
    unittest.main()
