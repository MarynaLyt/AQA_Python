"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""


class Student:
    def __init__(self, name: str, sur_name: str, age: int, average_score: float):
        self.name = name
        self.sur_name = sur_name
        self.age = age
        self.average_score = average_score

    def update_average_score(self, updated_score: float) -> str:
        self.average_score = updated_score
        return self.__str__()

    def __str__(self) -> str:
        return f"Студент: {self.name} {self.sur_name}, вік якого: {self.age} років, має середній бал: {self.average_score}"


student: Student = Student(name="Chandler", sur_name="Bing", age=26, average_score=75.5)
print(student.name)

print(student.update_average_score(85.2))
