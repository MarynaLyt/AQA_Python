numbers = [75, 99, 17, 46, 11, 55, 82, 86, 6, 5]
even_numbers = []

for numb in numbers:
    if numb % 2 == 0:
        even_numbers.append(numb)
print(sum(even_numbers))