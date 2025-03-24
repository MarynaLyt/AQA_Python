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

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
#
adwentures_of_tom_sawer = (adwentures_of_tom_sawer.replace("\n", " "))
print(adwentures_of_tom_sawer)
# # task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = (adwentures_of_tom_sawer.replace("....", ""))
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
split_text = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(split_text)
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_amount = adwentures_of_tom_sawer.count("h")
print(h_amount)

#
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
find_with_capital_letter = adwentures_of_tom_sawer.split()
for capital_letter in find_with_capital_letter:
    if capital_letter[0].istitle():
        count += 1
print(f"У тексті {count} слів починається з Великої літери")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_Tom_position = adwentures_of_tom_sawer.find("Tom")
second_Tom_position = adwentures_of_tom_sawer.find("Tom", first_Tom_position + 1)
print(f"Слово \"Tom\" вдруге pнайдено на позиції {second_Tom_position}.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_fourth_sentence
"""
adwentures_of_tom_sawer_fourth_sentence = adwentures_of_tom_sawer.split('. ')
print(adwentures_of_tom_sawer_fourth_sentence)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
# """
fourth_sentence = adwentures_of_tom_sawer_fourth_sentence[3]
lower_chapter = fourth_sentence.lower()
print(lower_chapter)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
for some_sentences in adwentures_of_tom_sawer_sentences:
    if some_sentences.startswith("By the time"):
        print("В тексті є речення яке починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
last_sentence = adwentures_of_tom_sawer_fourth_sentence[-1]
words = last_sentence.split()
word_count = len(words)
print(f"Речення складається з {word_count} слівю")