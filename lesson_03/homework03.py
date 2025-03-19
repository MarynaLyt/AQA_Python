alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," \
Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
 """
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area: int = 436402
azov_sea_area: int = 37800
total_ukrainian_seas_area = (black_sea_area+azov_sea_area)
print(f"Чорне та Азовське моря разом займають {total_ukrainian_seas_area} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
goods_first_and_second = 250449
goods_second_and_third = 222950
first_goods = total_goods - goods_second_and_third
second_goods = goods_first_and_second - first_goods
third_goods = goods_second_and_third - second_goods
print(f"Перший склад: {first_goods}\n" f"Другий склад: {second_goods}\n" f"Третій склад: {third_goods}\n")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

months = 18
monthly_payment = 1179
computer_cost = monthly_payment * months
print(f"Bартість комп’ютера складає: {computer_cost} грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"Остача від ділення 8019 на 8: {a}")
print(f"Остача від ділення 9907 на 9: {b}")
print(f"Остача від ділення 2789 на 5: {c}")
print(f"Остача від ділення 7248 на 6: {d}")
print(f"Остача від ділення 7128 на 5: {e}")
print(f"Остача від ділення 19224 на 9: {f}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_amount = 4
big_pizza_price = 274
total_big_pizza_price = big_pizza_amount * big_pizza_price 1096
middle_pizza_amount = 2
middle_pizza_price = 218
total_middle_pizza_price = middle_pizza_amount * middle_pizza_price 436
juice_amount = 4
juice_price = 35
total_juice_price = juice_amount * juice_price 140
cake_amount = 1
cake_price = 350
total_cake_price = cake_amount * cake_price 350
water_amount = 3
water_price = 21
total_water_price = water_amount * water_price 63
total = total_big_pizza_price + total_middle_pizza_price + total_juice_price + total_cake_price + total_water_price
print(f"Для данного замовлення знадобіться {total} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
fotos = 232
fotos_on_the_one_page = 8
pages = 232 // 8
print(f"Ігорю знадобиться {pages} сторінок, щоб вклеїти всі фото")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
gasoline_per_100_km = 9
tank_capacity = 48
gasoline_on_the_journey = (distance // 100) * gasoline_per_100_km
number_of_refills = (gasoline_on_the_journey // tank_capacity) - 1
print(f"{gasoline_on_the_journey} літрів бензину знадобиться для подорожі")
print(f"Родині потрібно заїхати на заправку {number_of_refills} рази")