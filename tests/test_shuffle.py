from arrayutilities import Arr
import unittest

class TestArr(unittest.TestCase):
    def test_shuffle_no_seed(self):
        test_array = [i for i in range(1, 25)]
        shuffled_array = Arr.shuffle(test_array)
        self.assertNotEqual(shuffled_array, test_array, "Should shuffle the array without a specified seed")

    def test_shuffle_with_seed(self):
        test_array = [i for i in range(1, 25)]
        seed = 42
        shuffled_array_1 = Arr.shuffle(test_array, seed)
        shuffled_array_2 = Arr.shuffle(test_array, seed)
        self.assertEqual(shuffled_array_1, shuffled_array_2, "Should produce the same shuffle with a specified seed")

    def test_shuffle_with_different_seeds(self):
        test_array = [i for i in range(1, 25)]
        shuffled_array_1 = Arr.shuffle(test_array, seed=1)
        shuffled_array_2 = Arr.shuffle(test_array, seed=50)
        self.assertNotEqual(shuffled_array_1, shuffled_array_2, "Should produce different shuffles with different seeds")

if __name__ == '__main__':
    unittest.main()
