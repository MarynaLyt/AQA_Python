import unittest
from lesson_09.functions import longest_word_in_the_list


class MyTestCase(unittest.TestCase):
    def test_str_value(self):
        inputs = [
            ["The sun sets behind the mountains, casting long shadows across the valley."],
            ["A gentle breeze whispers through the trees, carrying the scent of fresh rain."],
            ["Coffee and books make the perfect combination for a cozy afternoon."]
        ]
        for word in inputs:
            self.assertIsInstance(word[0], str)

    def test_empty_string(self):
        self.assertEqual(longest_word_in_the_list(""), "")

    def test_equal_length_words(self):
        self.assertEqual(longest_word_in_the_list("dog cat rat"), "dog")

    def test_single_word(self):
        self.assertEqual(longest_word_in_the_list("one"), "one")

    def test_numbers_in_words(self):
        self.assertEqual(longest_word_in_the_list("apple 1234567890 banana"), "1234567890")

