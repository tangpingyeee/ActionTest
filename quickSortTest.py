import unittest
from quicksort import quicksort

class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])
    
    def test_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(quicksort([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])
    
    def test_duplicate_elements(self):
        self.assertEqual(quicksort([5, 2, 8, 1, 3, 2, 5]), [1, 2, 2, 3, 5, 5, 8])

    def test_negative_numbers(self):
        self.assertEqual(quicksort([-5, 2, -8, 1, -3]), [-8, -5, -3, 1, 2])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            quicksort([5, '2', 8, 1, 3])

    def test_large_list(self):
        # Test sorting a large list of numbers
        input_list = list(range(10**6, 0, -1))
        expected_output = list(range(1, 10**6 + 1))
        self.assertEqual(quicksort(input_list), expected_output)

    def test_repeated_elements(self):
        # Test handling a list with many repeated elements
        input_list = [1] * 10**6 + [2] * 10**6
        expected_output = [1] * 10**6 + [2] * 10**6
        self.assertEqual(quicksort(input_list), expected_output)
        
if __name__ == '__main__':
    unittest.main()
    