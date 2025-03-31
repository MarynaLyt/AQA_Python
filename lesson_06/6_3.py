lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for data_type in lst1:
    if isinstance(data_type, str):
        lst2.append(data_type)
print(f"lst2 = {lst2}")