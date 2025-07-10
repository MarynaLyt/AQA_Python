# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenRange:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                val = self.current
                self.current += 1
                return val
            self.current += 1
        raise StopIteration