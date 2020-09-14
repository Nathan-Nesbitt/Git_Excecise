import unittest

from git_exercise import Sort

# hello
# Test

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

    def test_string_sort(self):
        """
            Tests to see if default functionality works.
        """
        sorted_array = ["apples", "bananas", "carrots", "oranges"]
        sort = Sort(["oranges", "carrots", "bananas", "apples"])

        self.assertEqual(sorted_array, sort.string_sort())

    def test_string_sort_type(self):
        """
            Tests to see if wrong data-types are caught.
        """
        sort = Sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertRaises(TypeError, sort.string_sort)

if __name__ == "__main__":
    unittest.main()