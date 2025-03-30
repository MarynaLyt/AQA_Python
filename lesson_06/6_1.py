new_str = input("Введіть значення: ")
unique_symbol = set(new_str)
lng_check = len(unique_symbol) >= 10
print(lng_check)