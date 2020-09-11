import unittest

from git_exercise import Sort


class TestSort(unittest.TestCase):

    def test_integer_sort(self):
        """
            Tests to see if default functionality works.
        """
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sort = Sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

        self.assertEqual(sorted_array, sort.interger_sort())

    def test_integer_sort_type(self):
        """
            Tests to see if wrong data-types are caught.
        """
        sort = Sort(["a", "b", "c"])
        self.assertRaises(TypeError, sort.interger_sort)

if __name__ == "__main__":
    unittest.main()