import csv
import os

directory = r'/Users/marynalytvynenko/cource/materials/13'
file1 = os.path.join(directory, 'random.csv')
file2 = os.path.join(directory, 'random-michaels.csv')


def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [tuple(row) for row in reader]
    return headers, data


headers1, data1 = read_csv(file1)
headers2, data2 = read_csv(file2)

combined_data = set(data1 + data2)

output_file = os.path.join(directory, 'result_Lytvynenko.csv')
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers1)
    writer.writerows(combined_data)

print(f"Результат записан в файл {output_file}")
