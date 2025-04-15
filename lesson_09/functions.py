def calculates_sum_of_numbers(a, b) -> int:
    """
    The function that calculates the sum of two numbers
    :return:
    """
    return a + b


def arithmetic_mean_of_numbers(a, b) -> float:
    """
    The function that calculates the arithmetic mean of a list of numbers
    :param a: srr
    :param b: str
    :return: arithmetic of entered numbers
    """
    arithmetic_of_numbers = (a + b) / 2
    return arithmetic_of_numbers


def longest_word_in_the_list(row: str) -> str:
    """
    The function that takes a list of words and returns the longest word in the list.
    :param row: str
    :return: str
    """
    words = row.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
