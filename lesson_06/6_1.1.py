new_str = input("Введіть значення: ")
unique_symbol = []
for symbol in new_str:
    if symbol not in unique_symbol:
        unique_symbol.append(symbol)
print(f"В даному тексті міститься {len(unique_symbol)} унікальних символів")