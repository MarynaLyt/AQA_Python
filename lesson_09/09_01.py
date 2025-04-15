import unittest
from lesson_09.functions import calculates_sum_of_numbers


class MyTestCase(unittest.TestCase):
    def test_passed_calculation(self) -> None:
        """
        Tests that the function correctly calculates the sum of two ints or float
        :return: None
        """
        self.assertEqual(3, calculates_sum_of_numbers(1, 2), msg="Entered value is not correct")
        self.assertIsInstance(calculates_sum_of_numbers(2.1, 2), int | float,
                              msg="Result should be of type int or float")

    def test_failed_with_TypeError(self) -> None:
        """
        Tests that the function raises a TypeError when one or both arguments are of incorrect type
        :return: None
        """
        invalid_inputs = [
            ("1", 1),
            (1, "2"),
            (None, 1),
            (1, None),
            ([1], 1),
            ({}, 2),
            (1, []),
            ([1, 2.2, 3], 3)
        ]
        for a, b in invalid_inputs:
            self.assertRaises(TypeError, calculates_sum_of_numbers, a, b, msg="This is not TypeError")

    def test_failed_with_AssertionError(self) -> None:
        """
        Tests that the function raises an AssertionError when one or both arguments are negative.
        :return: None
        """
        self.assertNotEqual(5, calculates_sum_of_numbers(1, -2))


if __name__ == '__main__':
    unittest.main()