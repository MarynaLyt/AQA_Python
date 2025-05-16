# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    """
    Initialize the appropriate variable
    :return: str
    """

    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number}x{multiplier}={result}")
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def calculates_sum_of_numbers() -> None:
    """
    The function that calculates the sum of two numbers
    :return:
    """
    sum_of_numbers = 3 + 6
    print(sum_of_numbers)


calculates_sum_of_numbers()


def calculates_sum_of_numbers(a, b) -> None:
    """
    The function that calculates the sum of two numbers
    :param a: first number
    :param b: second number
    :return: None
    """
    sum_of_numbers = a + b
    print(sum_of_numbers)


# Приклад виклику функції з аргументами
calculates_sum_of_numbers(3, 6)

#
# # task 3
# """  Написати функцію, яка розрахує середнє арифметичне списку чисел.
# """


def arithmetic_mean_of_numbers(a, b) -> float:
    """
    The function that calculates the arithmetic mean of a list of numbers
    :param a: srr
    :param b: str
    :return: arithmetic of entered numbers
    """
    arithmetic_of_numbers = (a + b) / 2
    return arithmetic_of_numbers


result = arithmetic_mean_of_numbers(2, 2)
print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def string_in_reverse_order(row: str) -> str:
    """
    The function that takes a string and returns it in reverse order
    :param row: str
    :return: str
    """
    return row[::-1]


result = string_in_reverse_order("Написати функцію, яка приймає рядок та повертає його у зворотному порядку")
print(result)


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_in_the_list(row: str) -> str:
    """
    The function that takes a list of words and returns the longest word in the list.
    :param row: str
    :return: str
    """
    words = row.split()  # Розбиваємо речення на список слів
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


list_of_words = "Написати функцію, яка приймає список слів та повертає найдовше слово у списку."
result = longest_word_in_the_list(list_of_words)
print(result)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2) -> int:
    """
    The  function that takes two rows and returns the index of the first occurrence of the second row to the first line if the second line is a substring of the first line, and -1 if the second lineis not a substring of the first line
    :param str1:str
    :param str2: str
    :return:int
    """
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# tasks form homework 4:
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_fourth_sentence
"""


# def adwentures_of_tom_sawer_fourth_sentence() -> list[str]:
#     """
#     The function splits the variable adwentures_of_tom_sawer by the end of a sentence and stores the result in the variable adwentures_of_tom_sawer_fourth_sentence.
#     :return: str
#     """
#     return adwentures_of_tom_sawer.split('. ')
#
#
# result = adwentures_of_tom_sawer_fourth_sentence()
# print(result)

# UPDATED:
def adwentures_of_tom_sawer_fourth_sentence(text: str) -> list[str]:
    """
    The function splits the input text by the end of a sentence.
    :param text: Input string
    :return: List of sentences
    """
    return text.split('. ')


result = adwentures_of_tom_sawer_fourth_sentence(adwentures_of_tom_sawer)
print(result)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.replace("....", "").replace("\n", " ").split())


def fourth_sentence() -> str:
    sentences = adwentures_of_tom_sawer.split(". ")
    return sentences[3].lower()


result_04 = fourth_sentence()
print(result_04)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
# """
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")


def check_sentences() -> str:
    """
    The function checks if any sentence begins with "By the time
    :return:str
    """
    for sentence in adwentures_of_tom_sawer_sentences:
        if sentence.startswith("By the time"):
            return "В тексті є речення, яке починається з 'By the time'"
    return "В тексті немає речення, яке починається з 'By the time'"


result_09 = check_sentences()
# print(result_09)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""


def calculate_amount_of_words():
    """
    Function that derives the number of words in the last sentence
    from the adwentures_of_tom_sawer_sentences.
    """
    last_sentence = adwentures_of_tom_sawer_sentences[-1]
    words = last_sentence.split()
    word_count = len(words)
    return f"Речення складається з {word_count} слів"


result_10 = calculate_amount_of_words()
print(result_10)
