import unittest
from lesson_09.functions import arithmetic_mean_of_numbers


class MyTestCase(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(2, arithmetic_mean_of_numbers(2, 2), msg="This is NOT even number")
        self.assertNotEqual(2, arithmetic_mean_of_numbers(1, 2), msg="This is EVEN number")

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
            self.assertRaises(TypeError, arithmetic_mean_of_numbers, a, b, msg="This is not TypeError")

