from arrayutilities import Arr
import unittest

class TestArrStrpos(unittest.TestCase):
    def test_strpos_single_needle_found(self):
        haystack = "hello world"
        needles = "world"
        result = Arr.strpos(haystack, needles)
        self.assertEqual(result, 6, "Should return the position of the first occurrence of the needle")

    def test_strpos_single_needle_not_found(self):
        haystack = "hello world"
        needles = "earth"
        result = Arr.strpos(haystack, needles)
        self.assertFalse(result, "Should return False when the needle is not found in the haystack")

    def test_strpos_multiple_needles_found(self):
        haystack = "hello world"
        needles = ["world", "ello"]
        result = Arr.strpos(haystack, needles)
        self.assertEqual(result, 1, "Should return the position of the first occurrence of any needle")

    def test_strpos_multiple_needles_not_found(self):
        haystack = "hello world"
        needles = ["earth", "moon"]
        result = Arr.strpos(haystack, needles)
        self.assertFalse(result, "Should return False when none of the needles are found in the haystack")

    def test_strpos_with_offset(self):
        haystack = "hello world hello"
        needles = "hello"
        offset = 6
        result = Arr.strpos(haystack, needles, offset)
        self.assertEqual(result, 12, "Should return the position of the first occurrence of the needle after the offset")

if __name__ == '__main__':
    unittest.main()
